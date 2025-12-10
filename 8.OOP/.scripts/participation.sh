#!/bin/sh

# --------------------------------------
#
# Participation report generator (Merged + main.py EXEC + requirements.txt)
#
# --------------------------------------

source ../.scripts/students.sh --source-only

# Convert numbers to emoji
num_to_emoji() {
    case "$1" in
        0) echo ":zero:" ;;
        1) echo ":one:" ;;
        2) echo ":two:" ;;
        3) echo ":three:" ;;
        4) echo ":four:" ;;
        5) echo ":five:" ;;
        6) echo ":six:" ;;
        7) echo ":seven:" ;;
        8) echo ":eight:" ;;
        9) echo ":nine:" ;;
        *) echo ":keycap_ten:" ;;
    esac
}

echo "# Participation au $(date +"%d-%m-%Y %H:%M")"
echo ""
echo "| Table des matières            | Description                                             |"
echo "|-------------------------------|---------------------------------------------------------|"
echo "| :a: [Présence](#a-présence)   | L'étudiant.e a fait son travail    :heavy_check_mark:   |"
echo "| :b: [Précision](#b-précision) | L'étudiant.e a réussi son travail  :tada:               |"
echo ""
echo "## Légende"
echo ""
echo "| Signe              | Signification                 |"
echo "|--------------------|-------------------------------|"
echo "| :heavy_check_mark: | Prêt à être corrigé           |"
echo "| :x:                | Projet inexistant             |"
echo "| :page_facing_up:   | requirements.txt présent      |"
echo "| :rocket:           | Script Python exécutable      |"
echo "| :receipt:          | Notebook présent              |"
echo "| :writing_hand:     | Signature dans le notebook    |"
echo "| :framed_picture:   | Figures présentes             |"
echo ""

echo "## :a: Présence"
echo ""
echo "|:hash:| Boréal :id: | README.md | images | :page_facing_up: req | :rocket: main.py | :receipt: RAPPORT | :writing_hand: Sgn | :framed_picture: Figures | :boom: Erreurs |"
echo "|------|-------------|-----------|--------|-------------------|-------------------|----------------|-----------|--------------------------|----------------|"

i=0
s=0
total_figures=0

for id in "${ETUDIANTS[@]}"
do
    URL="[<image src='https://avatars0.githubusercontent.com/u/${AVATARS[$i]}?s=460&v=4' width=20 height=20></image>](https://github.com/${IDS[$i]})"

    FILE=${id}/README.md
    FOLDER=${id}/images
    REQUIRE=${id}/requirements.txt
    REPORT=${id}/RAPPORT.ipynb
    MAIN=${id}/main.py

    README_ICON=":x:"
    IMAGES_ICON=":x:"
    REQUIRE_ICON=":x:"
    EXEC_PY_ICON=":x:"
    RAPPORT_ICON=":x:"
    SIGN_ICON=":x:"
    FIGURES_ICON=":zero:"
    ERROR_ICON=":x:"

    # README
    [ -f "$FILE" ] && README_ICON=":heavy_check_mark:"

    # images folder
    [ -d "$FOLDER" ] && IMAGES_ICON=":heavy_check_mark:"

    # requirements.txt
    [ -f "$REQUIRE" ] && REQUIRE_ICON=":page_facing_up:"

    # main.py execution
    if [ -f "$MAIN" ]; then
        python3 "$MAIN" > /dev/null 2>&1
        [ $? -eq 0 ] && EXEC_PY_ICON=":rocket:"
    fi

    # Notebook RAPPORT.ipynb
    if [ -f "$REPORT" ]; then
        RAPPORT_ICON=":receipt:"

        # Comptage des erreurs
        ERROR_COUNT=$(jq '[.cells[].outputs[]?
                           | select(.output_type=="error")] 
                         | length' "$REPORT" 2>/dev/null)

        [ "$ERROR_COUNT" -eq 0 ] && ERROR_ICON="" || ERROR_ICON=":boom:"

        # Comptage des Figures uniquement si pas d'erreur
        if [ "$ERROR_COUNT" -eq 0 ]; then
            FIGURES_COUNT=$(jq '[.cells[].outputs[]? 
                                  | select(.output_type=="display_data")
                                  | .data."text/plain"
                                  | .[] 
                                  | select(test("Figure"))] | length' "$REPORT" 2>/dev/null)

            FIGURES_ICON=$(num_to_emoji "$FIGURES_COUNT")
            total_figures=$((total_figures + FIGURES_COUNT))
        else
            FIGURES_COUNT=0
            FIGURES_ICON=":zero:"
        fi

        # Vérifier si l'ID est présent dans un markdown
        ID_PRESENT=$(jq -r --arg id "$id" '
                        .cells[] | select(.cell_type=="markdown")
                        | .source[] | select(test($id))' "$REPORT" 2>/dev/null)

        [ -n "$ID_PRESENT" ] && SIGN_ICON=":writing_hand:"
    fi

    echo "| ${i} | [${id}](../${FILE}) ${URL} | ${README_ICON} | ${IMAGES_ICON} | ${REQUIRE_ICON} | ${EXEC_PY_ICON} | [${RAPPORT_ICON}](../${REPORT}) | ${SIGN_ICON} | ${FIGURES_ICON} | ${ERROR_ICON} |"

    # Comptage minimal
    if [ "$README_ICON" = ":heavy_check_mark:" ] && \
       [ "$IMAGES_ICON" = ":heavy_check_mark:" ] && \
       [ "$RAPPORT_ICON" = ":receipt:" ]; then
        s=$((s+1))
    fi

    i=$((i+1))
done

COUNT="\$\\frac{${s}}{${i}}$"
STATS=$(echo "$s*100/$i" | bc)
SUM_EXEC="$\displaystyle\sum_{i=1}^{${i}} e_i$"

echo "| :abacus: | ${COUNT} = ${STATS}% | | | | | | | ${SUM_EXEC} = ${total_figures} |"


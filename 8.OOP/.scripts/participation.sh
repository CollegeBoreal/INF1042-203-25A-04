#!/bin/sh

# --------------------------------------
#
# Participation report generator (Merged + main.py EXEC restored)
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
echo "| :rocket:           | Script Python exécutable      |"
echo "| :receipt:          | Notebook présent              |"
echo "| :writing_hand:     | Signature dans le notebook    |"
echo ""

echo "## :a: Présence"
echo ""
echo "|:hash:| Boréal :id: | README.md | images | :rocket: main.py | :receipt: RAPPORT.ipynb | :writing_hand: Signature | :martial_arts_uniform: Exécutions | :boom: Erreurs |"
echo "|------|-------------|-----------|--------|-------------------|---------------|-----------|------------------------------------|----------------|"

i=0
s=0
total_exec=0

for id in "${ETUDIANTS[@]}"
do
    URL="[<image src='https://avatars0.githubusercontent.com/u/${AVATARS[$i]}?s=460&v=4' width=20 height=20></image>](https://github.com/${IDS[$i]})"

    FILE=${id}/README.md
    FOLDER=${id}/images
    REPORT=${id}/RAPPORT.ipynb
    MAIN=${id}/main.py

    README_ICON=":x:"
    IMAGES_ICON=":x:"
    EXEC_PY_ICON=":x:"
    RAPPORT_ICON=":x:"
    SIGN_ICON=":x:"
    EXEC_NOTEBOOK_ICON=":zero:"
    ERROR_ICON=":x:"

    # README
    [ -f "$FILE" ] && README_ICON=":heavy_check_mark:"

    # images folder
    [ -d "$FOLDER" ] && IMAGES_ICON=":heavy_check_mark:"

    # main.py execution
    if [ -f "$MAIN" ]; then
        python3 "$MAIN" > /dev/null 2>&1
        [ $? -eq 0 ] && EXEC_PY_ICON=":rocket:"
    fi

    # Notebook RAPPORT.ipynb
    if [ -f "$REPORT" ]; then
        RAPPORT_ICON=":receipt:"

        EXEC_COUNT=$(jq '[.cells[].outputs[]? 
                          | select(.output_type=="execute_result")] 
                         | length' "$REPORT" 2>/dev/null)
        EXEC_NOTEBOOK_ICON=$(num_to_emoji "$EXEC_COUNT")
        total_exec=$((total_exec + EXEC_COUNT))

        ERROR_COUNT=$(jq '[.cells[].outputs[]?
                           | select(.output_type=="error")] 
                         | length' "$REPORT")

        [ "$ERROR_COUNT" -eq 0 ] && ERROR_ICON="" || ERROR_ICON=":boom:"

        ID_PRESENT=$(jq -r --arg id "$id" '
                        .cells[] | select(.cell_type=="markdown")
                        | .source[] | select(test($id))' "$REPORT")

        [ -n "$ID_PRESENT" ] && SIGN_ICON=":writing_hand:"
    fi

    echo "| ${i} | [${id}](../${FILE}) ${URL} | ${README_ICON} | ${IMAGES_ICON} | ${EXEC_PY_ICON} | [${RAPPORT_ICON}](../${REPORT}) | ${SIGN_ICON} | ${EXEC_NOTEBOOK_ICON} | ${ERROR_ICON} |"

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

echo "| :abacus: | ${COUNT} = ${STATS}% | | | | | Total Exécutions = ${total_exec} | |"


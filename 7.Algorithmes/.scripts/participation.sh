#!/bin/sh

# --------------------------------------
#
# Participation report generator
#
# --------------------------------------

# Charger la liste des étudiants
source ../.scripts/students.sh --source-only

# Fonction pour convertir nombre → emoji
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
        *) echo ":keycap_ten:" ;;  # fallback pour > 9
    esac
}

# Titre
echo "# Participation au $(date +"%d-%m-%Y %H:%M")"
echo ""

# Table des matières
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
echo ""
echo "## :a: Présence"
echo ""
echo "|:hash:| Boréal :id:                | README.md    | images | RAPPORT.ipynb  | Signature | :martial_arts_uniform: Exécutions | :boom: Erreurs"
echo "|------|----------------------------|--------------|--------|----------------|-----------|--------|-----------|"

# Initialisation
i=0
s=0
total_exec=0

# Boucle sur tous les étudiants
for id in "${ETUDIANTS[@]}"
do
    URL="[<image src='https://avatars0.githubusercontent.com/u/${AVATARS[$i]}?s=460&v=4' width=20 height=20></image>](https://github.com/${IDS[${i}]})"
    FILE=${id}/README.md
    FOLDER=${id}/images
    REPORT=${id}/RAPPORT.ipynb

    # Initialisation des icônes
    README_ICON=":x:"
    IMAGES_ICON=":x:"
    RAPPORT_ICON=":x:"
    EXEC_ICON=":x:"
    ERROR_ICON=":x:"
    SIGN_ICON=":x:"

    # Vérification README
    if [ -f "$FILE" ]; then
        ACTUAL_NAME="$(basename "$(realpath "$FILE")")"
        if [ "$ACTUAL_NAME" = "README.md" ]; then
            README_ICON=":heavy_check_mark:"
        fi
    fi

    # Vérification images
    if [ -d "$FOLDER" ]; then
        IMAGES_ICON=":heavy_check_mark:"
    fi

    # Vérification RAPPORT.ipynb
    if [ -f "$REPORT" ]; then
        REPORT_NAME="$(basename "$(realpath "$REPORT")")"
        if [ "$REPORT_NAME" = "RAPPORT.ipynb" ]; then
            RAPPORT_ICON=":receipt:"
        fi

        # Nombre d'exécutions avec jq
        EXEC_COUNT=$(jq '[.cells[].outputs[]? 
                          | select(.output_type=="execute_result") 
                          | .data["text/plain"][]] 
                         | length' "$REPORT" 2>/dev/null)
        if [ $? -eq 0 ]; then
            EXEC_ICON=$(num_to_emoji "$EXEC_COUNT")
            total_exec=$((total_exec + EXEC_COUNT))
        fi

        # Nombre d'erreurs avec jq
        ERROR_COUNT=$(jq '[.cells[].outputs[]? 
                           | select(.output_type=="error")] 
                          | length' "$REPORT" 2>/dev/null)
        if [ $? -eq 0 ]; then
            if [ "$ERROR_COUNT" -eq 0 ]; then
                ERROR_ICON=""  # pas d'erreur
            else
                ERROR_ICON=":clock${ERROR_COUNT:-0}:"
            fi
        fi

        # Vérification de la présence de l'ID dans le notebook (Signature)
        ID_PRESENT=$(jq -r --arg id "$id" '.cells[]
                             | select(.cell_type=="markdown")
                             | .source[]
                             | select(test($id))' "$REPORT" 2>/dev/null)
        if [ -n "$ID_PRESENT" ]; then
            SIGN_ICON=":writing_hand:"
        fi
    fi

    # Affichage de la ligne pour l'étudiant
    echo "| ${i} | [${id}](../${FILE}) ${URL} | ${README_ICON} | ${IMAGES_ICON} | [${RAPPORT_ICON}](../${REPORT}) | ${SIGN_ICON} | ${EXEC_ICON} | ${ERROR_ICON} |"

    # Comptage pour statistiques
    if [ "$README_ICON" = ":heavy_check_mark:" ] && [ "$IMAGES_ICON" = ":heavy_check_mark:" ] && [ "$RAPPORT_ICON" = ":receipt:" ]; then
        s=$((s+1))
    fi

    i=$((i+1))
done

# Statistiques globales
COUNT="\$\\frac{${s}}{${i}}$"
STATS=$(echo "$s*100/$i" | bc)
SUM="$\displaystyle\sum_{i=1}^{${i}} s_i$"
SUM_EXEC="$\displaystyle\sum_{i=1}^{${i}} e_i$"

echo "| :abacus: | ${COUNT} = ${STATS}% | ${SUM} = ${s} | | | | ${SUM_EXEC} = ${total_exec}"


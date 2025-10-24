#!/bin/sh

# --------------------------------------
#
# Participation report generator
#
# --------------------------------------

source ../.scripts/students.sh --source-only

echo "# Participation au `date +"%d-%m-%Y %H:%M"`"
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

echo ""
echo "## :a: Présence"
echo ""
echo "|:hash:| Boréal :id:                | README.md    | images | RAPPORT.ipynb |"
echo "|------|----------------------------|--------------|--------|----------------|"

i=0
s=0

for id in "${ETUDIANTS[@]}"
do
   URL="[${IDS[${i}]}](https://github.com/${IDS[${i}]}) <image src='https://avatars0.githubusercontent.com/u/${AVATARS[$i]}?s=460&v=4' width=20 height=20></image>"
   FILE=${id}/README.md
   FOLDER=${id}/images
   REPORT=${id}/RAPPORT.ipynb

   README_ICON=":x:"
   IMAGES_ICON=":x:"
   RAPPORT_ICON=":x:"

   if [ -f "$FILE" ]; then
       ACTUAL_NAME="$(basename "$(realpath "$FILE")")"
       if [[ "$ACTUAL_NAME" == "README.md" ]]; then
           README_ICON=":heavy_check_mark:"
       fi
   fi

   if [ -d "$FOLDER" ]; then
       IMAGES_ICON=":heavy_check_mark:"
   fi

   if [ -f "$REPORT" ]; then
       RAPPORT_ICON=":receipt:"
   fi

   echo "| ${i} | [${id}](../${FILE}) :point_right: ${URL} | ${README_ICON} | ${IMAGES_ICON} | [${RAPPORT_ICON}](../${REPORT}) |"

   if [[ "$README_ICON" == ":heavy_check_mark:" && "$IMAGES_ICON" == ":heavy_check_mark:" && "$RAPPORT_ICON" == ":receipt:" ]]; then
       let "s++"
   fi

   let "i++"
   COUNT="\$\\frac{${s}}{${i}}$"
   STATS=$(echo "$s*100/$i" | bc)
   SUM="$\displaystyle\sum_{i=1}^{${i}} s_i$"
done

echo ""
echo "| :abacus: | " ${COUNT} " = " ${STATS}% "|" ${SUM} = ${s} "|"


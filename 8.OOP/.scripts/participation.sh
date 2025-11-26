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
echo "| :rocket:           | Exécution réussie             |"

echo ""
echo "## :a: Présence"
echo ""
echo "|:hash:| Boréal :id:                | README.md    | images | Execution |"
echo "|------|----------------------------|--------------|--------|-----------|"

i=0
s=0

for id in "${ETUDIANTS[@]}"
do
   URL="[<image src='https://avatars0.githubusercontent.com/u/${AVATARS[$i]}?s=460&v=4' width=20 height=20></image>](https://github.com/${IDS[${i}]})"
   FILE=${id}/README.md
   FOLDER=${id}/images
   MAIN=${id}/main.py

   README_ICON=":x:"
   IMAGES_ICON=":x:"
   EXEC_ICON=":x:"

   # README.md
   if [ -f "$FILE" ]; then
       ACTUAL_NAME="$(basename "$(realpath "$FILE")")"
       if [[ "$ACTUAL_NAME" == "README.md" ]]; then
           README_ICON=":heavy_check_mark:"
       fi
   fi

   # images folder
   if [ -d "$FOLDER" ]; then
       IMAGES_ICON=":heavy_check_mark:"
   fi

   # main.py execution test
   if [ -f "$MAIN" ]; then
      python3 "$MAIN" > /dev/null 2>&1
      if [ $? -eq 0 ]; then
         EXEC_ICON=":rocket:"
      else
         EXEC_ICON=":x:"
      fi
   fi

   echo "| ${i} | [${id}](../${FILE}) ${URL} | ${README_ICON} | ${IMAGES_ICON} | ${EXEC_ICON} |"

   # Count success if all icons are good
   if [[ "$README_ICON" == ":heavy_check_mark:" && "$IMAGES_ICON" == ":heavy_check_mark:" && "$EXEC_ICON" == ":rocket:" ]]; then
       let "s++"
   fi

   let "i++"
   COUNT="\$\\frac{${s}}{${i}}$"
   STATS=$(echo "$s*100/$i" | bc)
   SUM="$\displaystyle\sum_{i=1}^{${i}} s_i$"
done

echo "| :abacus: | " ${COUNT} " = " ${STATS}% "|" ${SUM} = ${s} "|"


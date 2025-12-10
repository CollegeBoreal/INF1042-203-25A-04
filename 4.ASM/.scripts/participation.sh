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
echo "|:hash:| Boréal :id:                | README.md    | images | riscv1.asm |"
echo "|------|----------------------------|--------------|--------|------------|"

i=0
s=0

for id in "${ETUDIANTS[@]}"
do
   URL="[<image src='https://avatars0.githubusercontent.com/u/${AVATARS[$i]}?s=460&v=4' width=20 height=20></image>](https://github.com/${IDS[${i}]})"
   FILE=${id}/README.md
   FOLDER=${id}/images
   RISCV=${id}/riscv1.asm

   # Présence des éléments
   HAS_README=":x:"
   HAS_IMAGES=":x:"
   HAS_RISCV=":x:"

   if [ -f "$FILE" ]; then
       ACTUAL_NAME="$(basename "$(realpath "$FILE")")"
       if [[ "$ACTUAL_NAME" == "README.md" ]]; then
           HAS_README=":heavy_check_mark:"
       fi
   fi

   if [ -d "$FOLDER" ]; then
       HAS_IMAGES=":heavy_check_mark:"
   fi

   if [ -f "$RISCV" ]; then
       HAS_RISCV=":heavy_check_mark:"
   fi

   # Ligne tableau
   echo "| ${i} | [${id}](../${FILE}) ${URL} | ${HAS_README} | ${HAS_IMAGES} | ${HAS_RISCV} |"

   # Statistiques
   if [ "$HAS_README" = ":heavy_check_mark:" ] && [ "$HAS_IMAGES" = ":heavy_check_mark:" ] && [ "$HAS_RISCV" = ":heavy_check_mark:" ]; then
       let "s++"
   fi

   let "i++"
   COUNT="\$\\frac{${s}}{${i}}$"
   STATS=$(echo "$s*100/$i" | bc)
   SUM="$\displaystyle\sum_{i=1}^{${i}} s_i$"
done
 
echo "| :abacus: | " ${COUNT} " = " ${STATS}% "|" ${SUM} = ${s} "|"


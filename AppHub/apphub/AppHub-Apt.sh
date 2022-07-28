#!/bin/bash


function transactionFeedback {

  actionString=("Install" "Uninstall")
  packageName=$1
   
               if [ "$2" = "1" ]; then       
                       zenity --error --text="An Error occured during ${actionString[mode]}ation!"
                      distrobox export --app $packageName --export-label "arch-appbox"         
               else 
                       zenity --info --text="${actionString[mode]}ation completed successfully." 
              distrobox export --app $packageName --export-label "arch-appbox"
            
          fi

}

function exportApp {

   $packageName=$1

  distrobox export --app $packageName --export-label "arch-appbox"

}


function transaction {
#mode to use for action
mode=$1
#action array

action=("-get install -y" " remove")
actionString=("Install" "Uninstall")
actionStringSimple=("Install" "Remove")
preparing=("Downloading Packages" "Preparing Removal")
preparation=("Download" "Preparation")


searchResult=$2

selected=$(zenity --list --title="App-Hub 1.0 Select Application Menu" --text="Select an Application to ${actionString[mode]}" --imagelist --ok-label=Select --cancel-label="Back" --print-column=2  --hide-header   --width=350 --height=350 \
  --column=""  \
  --column=""  \
   ${searchResult[@]}) || main


    apt show $selected | tr -s ' ' | zenity --text-info --width=500 --height=540  --title="Package Info for $selected " || search "$mode"
     

      zenity --question --text "Are you sure you want to ${actionString[mode]} the application?" --cancel-label="Cancel" --ok-label "${actionStringSimple[mode]} App"  --width=350  || search "$mode"   




          recursiveProgress | zenity  --progress --title="${actionString[mode]} Progress"  --text="${actionString[mode]}ing" --pulsate  --width=550  & instProgPID=$(echo  $!)


            sudo apt${action[mode]} $selected
 
    	    sleep 0.5
        	until [ ! $(pidof sudo) ]; do
        		sleep 0.5
        	done         

 
    
    kill -n $instProgPID  #kill infinate loop  
    transactionFeedback "$selected" "$mode"

	main
}

function recursiveProgress {


while true;
do
# echo "."
sleep 10   #sleep the infinate loop to not hog resources
done


}


function search {
# number repesenting search mode from passed parameter
mode=$1 
#array for search modes

searchTerm=$(zenity --entry --title="Find Apps." --width=350  --ok-label "Enter" --cancel-label "Back" --text="Type in as many keywords as you want to search for." ) || main

searchType=("apt search $searchTerm" "apt list --installed  | grep -v '^ ' | grep / | cut -d'/' -f1 | grep gnome
 $searchTerm")
# Array containing search searchResultults

if [ "$mode" = "0" ];
    then
searchResult=($(${searchType[mode]} $searchTerm | grep -v '^ ' | grep / | cut -d'/' -f1))
fi

if [ "$mode" = "1" ];
    then
searchResult=($(apt list --installed  | grep -v '^ ' | grep / | cut -d'/' -f1 | grep $searchTerm))
fi

# Check icons exist for search searchResultults
for ((i = 0; i < ${#searchResult[@]}; ++i)); do
 
icon="$HOME/Projects/Project/LinuxAppBox/AppHub/apphub/papirus-icon-theme-master/ePapirus-Dark/64x64/apps/${searchResult[i]}.svg"
if test -f "$icon";
then
   searchResult[i]="${icon} ${searchResult[i]}" 
# Format element to be the icon file path followed by the package name  
else
   searchResult[i]="$HOME/Projects/Project/LinuxAppBox/AppHub/apphub/noIcon.png ${searchResult[i]}"
# Insert place holder image
fi
done

#pass mode and searchResultult
transaction "$mode" "$searchResult"

}




function main {


table=(
$HOME/Projects/Project/LinuxAppBox/AppHub/apphub/papirus-icon-theme-master/ePapirus-Dark/64x64/apps/preferences-system-search.svg  "   Search and Install Apps"   "0"
$HOME/Projects/Project/LinuxAppBox/AppHub/apphub/papirus-icon-theme-master/ePapirus-Dark/64x64/places/trashcan_empty.svg
"    Find and Remove Apps"   "1")



selection=$(zenity --list --title="App-Hub 1.0 Main Menu" --text="Select an Option" --imagelist --ok-label=Select --cancel-label=Exit --print-column=3 --hide-column=3 --hide-header  --separator=' ' --width=350 --height=350 \
   --column=""  \
   --column="     "  \
   --column="     "  \
   "${table[@]}") || exit 

if [ "$selection" = "" ];
    then
       main
fi
search "$selection"

}

main

while true 
do
    echo "Press Enter to Start"
    read
    screencapture -R1380,220,500,150 screen.png  #Coordinates are selected as top right part of the screeen. Change accordingly
    tesseract screen.png tes #Using tesseract to do the ocr and save in tes.txt
    TES="$(<tes.txt)"
    python3 search.py "$TES" #Handing over to python3 for googling
    echo "Success!"
done

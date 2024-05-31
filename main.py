from getter import uploadCrossword
from publisher import postCrossword

if uploadCrossword():
    print("Crossword uploaded successfully")
    postCrossword()
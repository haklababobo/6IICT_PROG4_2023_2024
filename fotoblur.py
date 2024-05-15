import os, cv2

# Inladen alle bestanden in deze folder.
folder_pad    = r"YOLOdataset"
folder_inhoud = os.listdir(folder_pad)
 
# Overloop alle afbeeldingen in folder.
for index, bestand in enumerate(folder_inhoud):
    if (".png" in bestand) or (".jpg" in bestand): # We werken enkel met png- of jpg-bestanden.
       
        # Inladen afbeelding
        bestand_pad    = f"{folder_pad}/{bestand}"
        naam, extensie = os.path.splitext(bestand)
        afbeelding     = cv2.imread(bestand_pad)
 
        # Roteer afbeelding + opslaan.
        bestand_rotate = cv2.rotate(afbeelding, cv2.ROTATE_180)
        cv2.imwrite(filename=f'YOLOdataset/test/{naam}_rotate.{extensie}', img=bestand_rotate)
        # Spiegel afbeelding + opslaan.
        bestand_flip = cv2.flip(afbeelding, 0)
        cv2.imwrite(filename=f'YOLOdataset/test/{naam}_flip.{extensie}', img=bestand_flip)
 
        # Filter afbeelding (liefst wazig maken) + opslaan.
        bestand_blur = cv2.blur(afbeelding, (200,200))
        cv2.imwrite(filename=f'YOLOdataset/test/{naam}_blur.{extensie}', img=bestand_blur)
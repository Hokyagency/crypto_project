#from PIL import Image
#import piexif
from stegano import lsb


#def display_image_metadata(image_path):
#    with Image.open(image_path) as img:
#        print("\nMétadonnées de l'image :")
#        print(f"Format : {img.format}")
#        print(f"Mode : {img.mode}")
#        print(f"Taille : {img.size}")
#       print(f"Palette : {img.palette}")
#        print(f"Infos supplémentaires : {img.info}")


#def add_email_metadata(image_path, email):
#    try:
#        img = Image.open(image_path)
#        exif_dict = {"0th": {}, "Exif": {}, "GPS": {}, "1st": {}}
#        exif_dict["0th"][piexif.ImageIFD.ImageDescription] = f"Email: {email}"
#        exif_bytes = piexif.dump(exif_dict)
#        img.save(image_path, exif=exif_bytes)
#        print(f"\nEmail '{email}' ajouté aux métadonnées de l'image.")
#        
#    except Exception as e:
#        print(f"Erreur lors de l'ajout des métadonnées : {str(e)}")



#def main():
#    path = "test.jpg"
#    
#    # Afficher les métadonnées mises à jour
#    print("\nMétadonnées mises à jour :")
#    a = add_email_metadata("error_404.jpg", email= "email@email.com")
#    print(type(a))
#    print(add_email_metadata("error_404.jpg", email= "email@email.com"))
#
#
#if __name__ == "__main__":
#    main()


chemin_image = "ton_image.png"

description = "Ceci est une description ajoutée avec la bibliothèque stegano."
lsb.hide(chemin_image, description).save("image_avec_description.png")
print(f"La description a été ajoutée à 'image_avec_description.png'")

revealed_description = lsb.reveal("image_avec_description.png")
print(f"Description récupérée : {revealed_description}")
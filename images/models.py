# from django.db import models
from djongo import models
from django.contrib.auth.models import User
from keras.preprocessing.image import load_img, img_to_array
from keras.preprocessing import image
import numpy as np
import PIL.Image
from django.db.models import Count, F, Value
from tensorflow.keras.applications.inception_resnet_v2 import  InceptionResNetV2, decode_predictions, preprocess_input





# Create your models here
#In this class I am creating the image fucionality
class Image(models.Model):
    picture = models.ImageField(upload_to='picture')
    # blank == True makes teh field optional
    classField = models.CharField(max_length=200, blank=True)
    imageOwner = models.ForeignKey(User, related_name="image", on_delete=models.CASCADE, null=True)
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Image classified at {}".format(self.uploaded.strftime('%Y-%m-%d %H:%M'))

    #Retrive the image and make an analyses
    def save(self, *args, **kwargs):
        # Create a record to the db by saving the image
        super(Image, self).save(*args, **kwargs)
        print("Retrive image---> ", " Image ID: ", self.id , " Image Name: ", self.picture, " Image Path: ", self.picture.path)
        try:
            # I am using the load_img method from kerras to load the image is requiere to be self.picture.path
            image = PIL.Image.open(self.picture)
            img = load_img(self.picture.path, target_size=(299, 299))
            # Convert the image to an array of pixels
            img_array = img_to_array(img)
            # Convert the array to 4 dimensions
            to_pred = np.expand_dims(img_array, axis=0)
            # Preprocess the image for better results
            prep = preprocess_input(to_pred)
            model = InceptionResNetV2(weights='imagenet')
            prediction = model.predict(prep)
            decoded_prediction = decode_predictions(prediction)[0][0][1]
            decoded_prediction_all = decode_predictions(prediction)
            print("Prediction:  ", decoded_prediction, " All: ", decoded_prediction_all)
            self.classField = str(decoded_prediction)
            # Save the results to the record id that has been created above
            Image.objects.filter(id=self.id).update(classField= self.classField)
            print('success', "ClassField ")
        except ZeroDivisionError as e:
            img = e
            print('classification failed', img)


#User Class
class Lead(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    owner =models.ForeignKey(User, related_name="leads", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    #image=models.ManyToManyField(Image)


from django.db import models


class DesireInfo(models.Model):
    CustomerName = models.CharField(max_length=100,default="")
    CarName = models.CharField(max_length=100,default="")
    pdf = models.FileField(upload_to='info/pdfs/',default="")
    cover = models.ImageField(upload_to='info/covers/', null=True, blank=True,default="")

    def __str__(self):
        return self.CustomerName

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)

    def upload_CustomerName_blank(self):
        return(self.CustomerName != False)

    def CustomerName_char(self):
        punctuation=''
        return(self.CustomerName != punctuation)

    def image_blank(self):
        return(self.pdf != False)
    def cus(self):
        return(self.CarName != CustomerName)

    

    # def name(self):
    #     return(self.CustomerName == True)
    
    
   
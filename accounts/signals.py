from django.db.models.signals import post_save
from django.contrib.auth.models import User,Group
from accounts.models import Customer
def create_customer_profile(sender,instance,created,**kwargs):
    if created:
        #add customer gp as default for new user
        gp=Group.objects.get(name="customer")
        instance.groups.add(gp)
        #user.save()  
        #create customer_profile for user
        Customer.objects.create(user=instance,email=instance.email) #connect user from customer and user from register 

post_save.connect(create_customer_profile,sender=User)
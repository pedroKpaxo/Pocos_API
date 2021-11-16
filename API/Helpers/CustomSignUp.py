from allauth.account.forms import SignupForm
from django import forms

class ProfileSignUp(SignupForm):
    '''
    Boiler for the Custom profile uploads
    '''
    profilepic = forms.FileField(default=None)

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(ProfileSignUp, self).save(request)
        

        # Add your own processing here.

        # You must return the original result.
        return user
from django import forms

from study_buddy.classroom.models import Event


class AddEvent(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'event_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
                   'teacher': forms.TextInput(attrs={'class': 'form-control'}),
                   'description': forms.Textarea(attrs={'class': 'form-control'}),
                   'event_url': forms.URLInput(attrs={'class': 'form-control'}),
                   'school': forms.Select(attrs={'class': 'form-control'})

                   }

class EditEvent(AddEvent):
    pass

class DeleteEvent(forms.ModelForm):
    class Meta:
        model = Event
        fields = ()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance
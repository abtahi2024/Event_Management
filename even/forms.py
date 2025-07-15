from django import forms
from even.models import Category,Event, Participant


class StyleFormMixin:
    default_classes="border border-gray-300 w-screen p-3  rounded-lg shadow-sm focus:border-rose-500 focus:ring-purple-500"

    def apply_styled_widget(self):
        for field_name,field in self.fields.items():
            if isinstance(field.widget,forms.TextInput):
                field.widget.attrs.update({
                    'class':self.default_classes,
                    'placeholder':f"Enter{field.label.lower()}"
                })
            elif isinstance(field.widget,forms.Textarea):
                field.widget.attrs.update({
                    'class':self.default_classes,
                    'placeholder':f'Enter{field.label.lower()}'
                })
            elif isinstance(field.widget,forms.Select):
                field.widget.attrs.update({
                    'class':'border-2 border-gray-300 p-3 rounded-lg bg-gray-200 m-1',
                    'placeholder':f'Enter{field.label.lower()}'
                })
            elif isinstance(field.widget,forms.EmailInput):
                field.widget.attrs.update({
                    'class':self.default_classes,
                    'placeholder':f'Enter{field.label.lower()}'
                })
            elif isinstance(field.widget,forms.CheckboxSelectMultiple):
                field.widget.attrs.update({
                    'class':'space-y-2',
                    'placeholder':f'Enter{field.label.lower()}'
                })
            else:
                field.widget.attrs.update({
                    'class':self.default_classes
                })

class CatagoryForm(StyleFormMixin,forms.ModelForm):
    class Meta:
        model=Category
        fields=['name','description']
        widgets={
            'name':forms.TextInput(attrs={'class':'from-input'}),
            'description':forms.Textarea(attrs={'class':'form-textarea'})
        }
    
    def __init__(self,*arg,**kwarg):
        super().__init__(*arg,**kwarg)
        self.apply_styled_widget()



class EventForm(StyleFormMixin,forms.ModelForm):
    class Meta:
        model=Event
        fields=['name','description','date','time','location','category']
        widgets={
            'date':forms.DateInput(attrs={'type': 'date', 'class': 'form-input'}),
            'time':forms.TextInput(attrs={'type': 'time', 'class': 'form-input'}),
            
        }
    def __init__(self,*arg,**kwarg):
        super().__init__(*arg,**kwarg)
        self.apply_styled_widget()
        self.fields['category'].empty_label='Select a category'

class ParticipantForm(StyleFormMixin,forms.ModelForm):
    class Meta:
        model=Participant
        fields=['name','email','events']

    def __init__(self,*arg,**kwarg):
        super().__init__(*arg,**kwarg)
        self.apply_styled_widget()
    
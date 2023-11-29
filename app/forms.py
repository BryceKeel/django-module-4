from django import forms


class NameForm(forms.Form):
    input_name = forms.CharField()


class BirthForm(forms.Form):
    birthyear = forms.IntegerField()
    ageyear = forms.IntegerField()


class BurgerForm(forms.Form):
    Burger = forms.IntegerField()
    Fries = forms.IntegerField()
    Drink = forms.IntegerField()
class FontForm(forms.Form):
    str_1 = forms.CharField()
    num_1 = forms.IntegerField()

class TeenForm(forms.Form):
    int_value1 = forms.IntegerField()
    int_value2 = forms.IntegerField()
    int_value3 = forms.IntegerField()

class xyzForm(forms.Form):
    xyz_string = forms.CharField()

class averageForm(forms.Form):
    val_1 = forms.IntegerField(required=True)
    val_2 = forms.IntegerField(required=True)
    val_3 = forms.IntegerField(required=True)
    val_4 = forms.IntegerField(required=False)
    val_5 = forms.IntegerField(required=False)
    val_6 = forms.IntegerField(required=False)
    val_7 = forms.IntegerField(required=False)
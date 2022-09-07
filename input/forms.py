from django import forms

PCLASS = (
        (1, 'First Class'),
        (2, 'Second Class'),
        (3, 'Third Class'),
    )
SEX = (
        (1, 'Male'),
        (0, 'female'),

    )
SIBSP = (
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 8),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
    )
PARCH = (
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 8),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
    )
EMBARKED = (
        (0, 'Southampton'),
        (1, 'Queenstown'),
        (2, 'Cherbourg'),
    )
TITLE = (
        (0, 'Mr'),
        (1, 'Mrs'),
        (2, 'Miss'),
        (3, 'Master'),
        (4, 'Don'),
        (5, 'Rev'),
        (6, 'Dr'),
        (7, 'Mmme'),
        (8, 'Ms'),
        (9, 'Major'),
        (10, 'Lady'),
        (11, 'Sir'),
        (12, 'Mlle'),
        (13, 'Col'),
        (14, 'Capt'),
        (15, 'the Countess'),
        (16, 'Jonkheer'),
    )
CHILD = (
        (0, 'Adult'),
        (1, 'Child'),
    )
CREW = (
        (0, 'Passenger'),
        (1, 'Crew'),

    )
class IndexForm(forms.Form):
    Pclass = forms.ChoiceField(choices=PCLASS,required=True)
    Sex = forms.ChoiceField(choices=SEX,required=True)
    Age = forms.IntegerField(required=True)
    SibSp = forms.ChoiceField(choices=SIBSP,required=True)
    Parch = forms.ChoiceField(choices=PARCH,required=True)
    Fare = forms.IntegerField(required=True)
    Embarked = forms.ChoiceField(choices=EMBARKED,required=True)
    Title = forms.ChoiceField(choices=TITLE,required=True)
    Child = forms.ChoiceField(choices=CHILD,required=True)
    Crew = forms.ChoiceField(choices=CREW,required=True)

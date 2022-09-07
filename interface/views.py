from django.views.generic import TemplateView
from django.shortcuts import render , redirect
from input.forms import IndexForm
import pandas as pd
import joblib
from .apps import InterfaceConfig
from input.params import y_column_name


class Index(TemplateView):
    template_name = 'interface/index.html'

    def get(self, request, *args, **kwargs):
        form = IndexForm()
        return render(request,self.template_name, {'form':form})

    def post(self,request):
        form = IndexForm(request.POST)
        if form.is_valid():
            Pclass = form.cleaned_data['Pclass']
            Sex = form.cleaned_data['Sex']
            Age = form.cleaned_data['Age']
            SibSp = form.cleaned_data['SibSp']
            Parch = form.cleaned_data['Parch']
            Fare = form.cleaned_data['Fare']
            Embarked = form.cleaned_data['Embarked']
            Title = form.cleaned_data['Title']
            Child = form.cleaned_data['Child']
            Crew = form.cleaned_data['Crew']


            if 'predict' in request.POST:
                X = {'X':[
                    Pclass, 
                    Sex, 
                    Age, 
                    SibSp, 
                    Parch, 
                    Fare, 
                    Embarked, 
                    Title, 
                    Child, 
                    Crew
                    
                    ]}
                X = pd.DataFrame(X)
                X = X.transpose()
                mdl = InterfaceConfig.model
                Y = mdl.predict(X)
                result =Y 
                result = pd.DataFrame(Y, columns = [y_column_name])
                result = result.replace({1:'Passenger Survives', 0:'Passenger Does not Survive'})

                result = result.to_csv(header=None,index=False)
            form = IndexForm()
        args = {'form': form , 'result':result}
        return render(request, self.template_name, args)
from django.shortcuts import render
from .forms import InputForm
# Create your views here.
def home_view(request):
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            y_name=request.POST.get('your_name')
            p_name=request.POST.get('person_name')
            flames=['f','l','a','m','e','s']
            name_1=list(y_name.lower())
            name_2=list(p_name.lower())
            count=0
            name2=name_2.copy()
            context={}
            for i in name_1:
                if i in name_2:
                    name_2.remove(i)
                    count+=1
            result=(len(name_1)-count)+len(name_2)
            while len(flames)!=1:
                x=len(flames)
                index=result%x
                if index==0:
                    index=x-1
                else:
                    index-=1
                flames=flames[index+1:]+flames[:index]
            relation=flames[0]
            name_1=("".join(name_1))
            name_2=("".join(name2))
            if relation=='f':
                context['result']=name_1.upper()+" and "+name_2.upper()+" You both are Friends."
            elif relation=='l':
                context['result']=name_1.upper()+" and "+name_2.upper()+" You both Love each other. Keep Loving."
            elif relation=='a':
                context['result']=name_2.upper()+" has a deep Affection for you."
            elif relation=='m':
                context['result']=name_1.upper()+" and "+name_2.upper()+" You both will Marry each other."
            elif relation=='e':
                context['result']="Dear "+name_1.upper()+", "+name_2.upper()+" is your Enemy. Try to create affection between you."
            elif relation=='s':
                context['result']="Dear "+name_1.upper()+", "+name_2.upper()+" is your Sibling."
            form.save()
            context['form']=form
            return render(request,'flames/homepage.html',context)
    else:
        form = InputForm()
    context={'form':form}
    return render(request,'flames/homepage.html',context)

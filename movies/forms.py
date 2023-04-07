from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
#     CHOICES = [
#     ('공포','공포'),('로맨스','로맨스'),('코미디','코미')
# ]
#     release_date = forms.DateField(widget=forms.DateInput)
#     score = forms.FloatField(widget=forms.NumberInput(attrs={'step':0.5, 'min':0, 'max':5}))
#     genre = forms.ChoiceField(choices = CHOICES, widget=forms.Select())
    class Meta:
        model = Movie
        fields = '__all__'
        

# genre 필드 > select element를 출력. 코미디, 공포, 로맨스 장르 선택가능
# score 필드 > input element type은 number
#         input element attribute 중 step은 0.5, min은 0, max는 5로 설정합니다.
# release_date 필드
# I. input element의 type은 date로 설정합니다.


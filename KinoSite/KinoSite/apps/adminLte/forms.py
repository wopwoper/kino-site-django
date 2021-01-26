from . import models
from django.forms import Form, ModelForm, TextInput, DateInput, FileInput, URLInput, CheckboxInput, Textarea, \
    EmailField, CharField, PasswordInput, ImageField, ModelChoiceField, URLField, ChoiceField, TimeField, BooleanField, RadioSelect, NumberInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(Form):
    class Meta:
        model = User

    username = CharField(widget=TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Username',
            }))
    password = CharField(widget=TextInput(attrs={
                'type': 'password',
                'class': 'form-control',
                'placeholder': 'Password',
            }))


class FilmForm(ModelForm):
    class Meta:
        model = models.Film
        fields = ['title', 'description', 'main_image', 'image1',
                  'image2', 'image3', 'image4', 'image5', 'trailer_link',
                  'two_d', 'three_d', 'i_max', 'duration', 'first_night']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название фильма',
                'id': 'FilmNameInput',
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'id': 'FilmTextInput',
                'rows': '5',
                'placeholder': 'Введите описание фильма',
            }),
            'main_image': FileInput(attrs={
                'class': 'form-control-file',
                'id': 'FilmPoster',
            }),
            'image1': FileInput(attrs={
                'class': 'form-control-file col-md-3 pl-0'
            }),
            'image2': FileInput(attrs={
                'class': 'form-control-file col-md-3'
            }),
            'image3': FileInput(attrs={
                'class': 'form-control-file col-md-3'
            }),
            'image4': FileInput(attrs={
                'class': 'form-control-file col-md-3'
            }),
            'image5': FileInput(attrs={
                'class': 'form-control-file col-md-3'
            }),
            'two_d': CheckboxInput(attrs={
                'name': 'two_d',
                'class': 'form-check-input',
                'type': 'checkbox',
                'id': 'inlineCheckbox1',
                'value': 'True',
            }),
            'three_d': CheckboxInput(attrs={
                'name': 'three_d',
                'class': 'form-check-input',
                'type': 'checkbox',
                'id': 'inlineCheckbox2',
                'value': 'True',
            }),
            'i_max': CheckboxInput(attrs={
                'name': 'i_max',
                'class': 'form-check-input',
                'type': 'checkbox',
                'id': 'inlineCheckbox3',
                'value': 'True',
            }),
            'duration': TextInput(attrs={
                'placeholder': 'Пример: 1 час 53 минуты',
                'class': 'form-control',
                'id': 'FilmDuration',
            }),
            'trailer_link': URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ссылку. Пример: https://www.youtube.com/watch...',
                'id': 'TrailerName',
            }),
            'first_night': DateInput(attrs={
                'type': "date",
                'placeholder': "Введите дату премьеры",
                'class': "form-control",
                'id': "FilmFirstNightDate",
        }),

        }


class CinemaForm(ModelForm):
    class Meta:
        model = models.Cinema
        fields = ['cinema_name', 'cinema_description', 'cinema_condition', 'cinema_logo', 'cinema_upper_banner',
                  'cinema_image1', 'cinema_image2', 'cinema_image3', 'cinema_image4', 'cinema_image5']

        widgets = {
            'cinema_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название кинотеатра',
                'id': 'CinemaNameInput',
            }),
            'cinema_description': Textarea(attrs={
                'class': 'form-control',
                'id': 'CinemaDescriptionInput',
                'rows': '5',
                'placeholder': 'Введите описание кинотеатра',
            }),
            'cinema_condition': Textarea(attrs={
                'class': 'form-control',
                'id': 'CinemaConditionInput',
                'rows': '5',
                'placeholder': 'Введите условия кинотеатра',
            }),
            'cinema_logo': FileInput(attrs={
                'class': 'form-control-file col-md-3 pl-0',
                'id': 'CinemaLogoInput',
            }),
            'cinema_upper_banner': FileInput(attrs={
                'class': 'form-control-file col-md-3 pl-0',
                'id': 'CinemaUpperBannerInput',
            }),
            'cinema_image1': FileInput(attrs={
                'class': 'form-control-file col-md-3 pl-0'
            }),
            'cinema_image2': FileInput(attrs={
                'class': 'form-control-file col-md-3'
            }),
            'cinema_image3': FileInput(attrs={
                'class': 'form-control-file col-md-3'
            }),
            'cinema_image4': FileInput(attrs={
                'class': 'form-control-file col-md-3'
            }),
            'cinema_image5': FileInput(attrs={
                'class': 'form-control-file col-md-3'
            })}


class CinemaHallForm(ModelForm):
    class Meta:
        model = models.CinemaHall
        cinema = ModelChoiceField(queryset=models.Cinema.objects.all(), empty_label=None, to_field_name="cinema_name")
        fields = ['cinema', 'hall_name', 'hall_description', 'hall_scheme', 'hall_upper_banner',
                  'hall_image1', 'hall_image2', 'hall_image3', 'hall_image4', 'hall_image5']

        widgets = {
            'hall_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название кинотеатра',
                'id': 'HallNameInput',
            }),
            'hall_description': Textarea(attrs={
                'class': 'form-control',
                'id': 'HallDescriptionInput',
                'rows': '5',
                'placeholder': 'Введите описание кинотеатра',
            }),
            'hall_scheme': FileInput(attrs={
                'class': 'form-control-file col-md-3 pl-0',
                'id': 'HallSchemeInput',
            }),
            'hall_upper_banner': FileInput(attrs={
                'class': 'form-control-file col-md-3 pl-0',
                'id': 'HallUpperBannerInput',
            }),
            'hall_image1': FileInput(attrs={
                'class': 'form-control-file col-md-3 pl-0'
            }),
            'hall_image2': FileInput(attrs={
                'class': 'form-control-file col-md-3'
            }),
            'hall_image3': FileInput(attrs={
                'class': 'form-control-file col-md-3'
            }),
            'hall_image4': FileInput(attrs={
                'class': 'form-control-file col-md-3'
            }),
            'hall_image5': FileInput(attrs={
                'class': 'form-control-file col-md-3'
            })}


class NewsForm(ModelForm):
    class Meta:
        model = models.News

        fields = ['news_name', 'news_description', 'news_main_image', 'news_image1', 'news_image2', 'news_image3',
                  'news_image4', 'news_image5', 'news_url', 'news_published_date', 'news_status']

        widgets = {
            'news_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название новости',
                'id': 'NewsNameInput',
            }),
            'news_description': Textarea(attrs={
                'class': 'form-control',
                'id': 'NewsTextInput',
                'rows': '5',
                'placeholder': 'Введите описание новости',
            }),
            'news_main_image': FileInput(attrs={
                'class': 'form-control-file',
                'id': 'NewsMainImage',
            }),
            'news_image1': FileInput(attrs={
                'class': 'form-control-file col-md-3 pl-0'
            }),
            'news_image2': FileInput(attrs={
                'class': 'form-control-file col-md-3'
            }),
            'news_image3': FileInput(attrs={
                'class': 'form-control-file col-md-3'
            }),
            'news_image4': FileInput(attrs={
                'class': 'form-control-file col-md-3'
            }),
            'news_image5': FileInput(attrs={
                'class': 'form-control-file col-md-3'
            }),
            'news_url': URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ссылку на новость',
                'id': 'NewsUrl',
            }),
            'news_published_date': DateInput(attrs={
                'type': "date",
                'placeholder': "Введите дату публикации",
                'class': "form-control",
                'id': "NewsPublishedDate",
            }),
        }


class UserForm(ModelForm):
    class Meta:
        model = models.User
        fields = ['name', 'surname', 'phone', 'username', 'email', 'address', 'password', 'password2', 'card_number',
                  'language', 'gender', 'city', 'date_of_birth', 'gender']

        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'id': "InputName",
            }),
            'surname': TextInput(attrs={
                'class': "form-control",
                'id': "InputSurname",
            }),
            'username': TextInput(attrs={
                'class': "form-control",
                'id': "InputUsername",
            }),
            'phone': TextInput(attrs={
                'class': "form-control",
                'id': "InputPhone",
            }),
            'email': TextInput(attrs={
                'class': "form-control",
                'id': "InputEmail",
                'type': "email",
            }),
            'date_of_birth': DateInput(attrs={
                'type': "date",
                'placeholder': "Введите дату рождения",
                'class': "form-control",
                'id': "InputDate",
            }),
            'address': TextInput(attrs={
                'class': "form-control",
                'id': "InputAddress",
            }),
            'password': TextInput(attrs={
                'class': "form-control",
                'id': "InputPassword",
                'placeholder': "Введите пароль",
            }),
            'password2': TextInput(attrs={
                'class': "form-control",
                'id': "InputPassword2",
                'placeholder': "Введите пароль",
            }),
            'card_number': TextInput(attrs={
                'class': "form-control",
                'id': "InputCardNumber",
                'placeholder': "Пример: 1234 5678 9012 3456"
            }),
            'gender': RadioSelect(attrs={
                'class': 'custom-control-input  custom-control-label',
            }),
            'language': RadioSelect(attrs={
                'class': 'custom-control-input  custom-control-label',
            })
        }
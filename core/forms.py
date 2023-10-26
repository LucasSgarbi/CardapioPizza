from django import forms
from django.core.mail.message import EmailMessage


class ContatoForms(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='email', max_length=150)
    assunto = forms.CharField(label='Assunto', max_length=100)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea(), max_length=300)

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome:{nome}\nE-mail:{email}\nAssunto:{assunto}\nMensagem:{mensagem}'

        mail = EmailMessage(
            subject=assunto,
            body=conteudo,
            from_email='lapeppo@pizzas.com.br',
            to=['lapeppo@pizzas.com.br', ],
            headers={'Reply-To': email}
        )
        mail.send()
from models import Aluno

def coletaDado(request):
    nome = request.POST.get("nome")
    cpf = request.POST.get("cpf")
    data = request.POST.get("data_nasc")
    end = request.POST.get("endereco")
    tel = request.POST.get("telefone")
    curso = request.POST.get("curso")

    nomeB = Aluno.objects.get(nome=nome)
    cpfB = Aluno.objects.get(cpf=cpf)
    dataB = Aluno.objects.get(data_nasc=data)
    endB = Aluno.objects.get(endereco=end)
    telB = Aluno.objects.get(telefone=tel)
    cursoB = Aluno.objects.get(curso=curso)

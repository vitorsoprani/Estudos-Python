import cv2

cap = cv2.VideoCapture(0)  # Indica qual vídeo ou câmera será lido.

# classe que pega o fourcc Code
fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
out = cv2.VideoWriter('output.avi', fourcc, 24, (640, 480)
                      )  # classe que salva os vídes.
# Argumentos: nome, fourcc code (especifica o codec???), fps, tmanho (largura, altura)


# a instancia gerada anteriormente possui alguns métodos úteis
# como este, que checa se o video está aberto ou não
print(cap.isOpened())
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # há muitos métodos úteis.
# o método .get pode retornar muitas informações, checar documentação.
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
while (cap.isOpened()):
    # 'ret' armazena o retorno de 'cap.read'(True ou False). 'frame' armazena o framne (imagem) em si
    ret, frame = cap.read()

    if ret:
        out.write(frame)  # método que efetivamente salva (escreve) o vídeo

        # métoodo que converte a imagem para um novo espectro de cor.
        # nesse caso converte de rgb para escala de cinza.
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('webcam', gray)  # exibe a imagem

        # a cada milisegundo(tempo arbitrario), checa se a tecla foi apertada
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break  # sai do loop
    else:
        break
# "libera os recursos", não entendi muito bem, perguntar para veteranos.
cap.release()
out.release()  # "libera os recursos"
cv2.destroyAllWindows()  # fecha as janelas.

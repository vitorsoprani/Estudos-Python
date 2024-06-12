import cv2

cap = cv2.VideoCapture(0)  # Indica qual vídeo ou câmera será lido.

# a instancia gerada anteriormente possui alguns métodos úteis
# como este, que checa se o video está aberto ou não
print(cap.isOpened())
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # há muitos métodos úteis.
# o método .get pode retornar muitas informações, checar a documentação.
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
while (cap.isOpened()):
    # 'ret' armazena o retorno de 'cap.read'(True ou False). 'frame' armazena o framne (imagem) em si
    ret, frame = cap.read()

    # métoodo que converte a imagem para um novo espectro de cor. nesse caso converte de rgb para escala de cinza.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('webcam', gray)  # exibe a imagem

    # a cada milisegundo(tempo arbitrario), checa se a tecla foi apertada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break  # sai do loop

# "libera os recursos", não entendi muito bem, perguntar para veteranos.
cap.release()
cv2.destroyAllWindows()  # fecha as janelas.

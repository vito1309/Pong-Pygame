# Pong — Refatorado com Princípios SOLID

Refatoramento do clássico jogo Pong desenvolvido em Python com pygame, aplicando boas práticas de engenharia de software.

---

## Tecnologias

- Python 3
- Pygame

---

## Como rodar

```bash
# Crie e ative o ambiente virtual
python -m venv venv
source venv/Scripts/activate  # Windows (Git Bash)

# Instale as dependências
pip install pygame

# Execute o jogo
python main.py
```

---

## Controles

| Ação | Tecla |
|---|---|
| Mover para cima | ↑ |
| Mover para baixo | ↓ |
| Iniciar jogo | Espaço |
| Jogar novamente | Espaço |
| Voltar ao menu | ESC |

---

## Estrutura do projeto

```
pong/
├── main.py           # Ponto de entrada da aplicação
├── settings.py       # Constantes e configurações globais
├── game.py           # Orquestra o fluxo entre as cenas
├── ball.py           # Entidade da bola
├── paddle.py         # Entidade da raquete
├── scoreboard.py     # Placar e condição de vitória
├── ai_controller.py  # Lógica de movimento da IA
└── renderer.py       # Todo o desenho na tela
```

---

## Conceitos aplicados

### Abstração
Cada arquivo representa um conceito real e isolado do jogo. `Bola` cuida apenas da bola, `Raquete` cuida apenas da raquete, e assim por diante. Nenhuma classe precisa saber como a outra funciona por dentro.

### Separação de responsabilidades
O `renderer.py` é o único arquivo que chama `pygame.draw`. O `scoreboard.py` é o único que conhece a pontuação necessária para vencer. O `game.py` coordena as entidades sem saber como elas são desenhadas.

### SOLID

**S — Single Responsibility:** cada classe tem exatamente uma razão para mudar. `Bola` muda se a física mudar, `Renderer` muda se o visual mudar.

**O — Open/Closed:** para criar uma IA com dificuldade diferente basta criar uma nova classe, sem modificar `ControladorIA` ou qualquer outro arquivo.

**L — Liskov Substitution:** `ControladorIA` pode ser substituída por qualquer outro controlador sem impacto no `game.py`.

**I — Interface Segregation:** cada classe recebe apenas o que precisa. A IA recebe `Raquete` e `Bola`, não o objeto `Jogo` inteiro.

**D — Dependency Inversion:** `Jogo` depende das entidades (`Bola`, `Raquete`), não de lógica concreta de desenho ou IA.

### Legibilidade
Todas as constantes estão nomeadas no `settings.py`, sem números mágicos espalhados no código. Nomes descritivos em português seguindo o padrão PEP 8.

### Documentação
Todas as classes e métodos possuem docstrings explicando sua responsabilidade.

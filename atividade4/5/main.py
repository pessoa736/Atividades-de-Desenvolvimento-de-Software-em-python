# crditos para essa questão: chatgpt.


import random
import time
import json
import os
import logging
from datetime import datetime

try:
    import nltk
    from nltk.corpus import wordnet
    nltk.data.find('corpora/wordnet')
except (ImportError, LookupError):
    nltk = None

try:
    from colorama import init, Fore, Style
    init(autoreset=True)
except ImportError:
    class Fore:
        RED = ''
        GREEN = ''
        YELLOW = ''
        CYAN = ''
        MAGENTA = ''
        WHITE = ''

    class Style:
        BRIGHT = ''
        RESET_ALL = ''

# Configuração do registro de logs
date_str = datetime.now().strftime("%Y%m%d_%H%M%S")
logging.basicConfig(
    filename=f'game_{date_str}.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class WordList:
    WORDS = {
        'Easy': ['maçã', 'cadeira', 'casa', 'rato', 'verde'],
        'Medium': ['python', 'pirâmide', 'rede', 'gravidade', 'quântica'],
        'Hard': ['síncrono', 'mnemônico', 'quiz', 'xilofone', 'zéfiro']
    }

    @classmethod
    def get_random_word(cls, difficulty):
        return random.choice(cls.WORDS.get(difficulty, []))

class HintSystem:
    def __init__(self, word):
        self.word = word
        self.hints_given = 0
        self.letters_revealed = set()

    def get_hint(self):
        self.hints_given += 1
        if self.hints_given == 1:
            return self._reveal_letter()
        elif self.hints_given == 2:
            return self._scramble()
        elif self.hints_given == 3 and nltk:
            return self._definition()
        return "Não há mais dicas disponíveis."

    def _reveal_letter(self):
        available = [c for c in set(self.word) if c not in self.letters_revealed]
        if not available:
            return "Todas as letras já foram reveladas."
        letter = random.choice(available)
        self.letters_revealed.add(letter)
        return f"Letra revelada: {letter}"

    def _scramble(self):
        scrambled = ''.join(random.sample(self.word, len(self.word)))
        return f"Palavra embaralhada: {scrambled}"

    def _definition(self):
        synsets = wordnet.synsets(self.word)
        if not synsets:
            return "Nenhuma definição encontrada."
        return f"Definição: {synsets[0].definition()}"

class HighScoreManager:
    FILE_PATH = 'highscores.json'

    def __init__(self):
        self.scores = self._load_scores()

    def _load_scores(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, 'r') as f:
            return json.load(f)

    def add_score(self, player_name, score, difficulty, time_taken):
        entry = {
            'name': player_name,
            'score': score,
            'difficulty': difficulty,
            'time': round(time_taken, 2),
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.scores.append(entry)
        self._save_scores()

    def _save_scores(self):
        with open(self.FILE_PATH, 'w') as f:
            json.dump(self.scores, f, indent=4)

    def display_scores(self):
        if not self.scores:
            print(Fore.YELLOW + "Ainda não há recordes.")
            return
        sorted_scores = sorted(self.scores, key=lambda x: x['score'], reverse=True)
        print(Fore.CYAN + Style.BRIGHT + "=== Melhores Pontuações ===")
        for entry in sorted_scores[:10]:
            print(f"{entry['date']} - {entry['name']} - {entry['difficulty']} - Pontos: {entry['score']} - Tempo: {entry['time']}s")

class Game:
    BASE_SCORES = {'Easy': 100, 'Medium': 200, 'Hard': 300}
    MAX_ATTEMPTS = {'Easy': 10, 'Medium': 7, 'Hard': 5}

    def __init__(self, player_name, difficulty):
        self.player = player_name
        self.difficulty = difficulty
        self.secret_word = WordList.get_random_word(difficulty)
        self.attempts_left = self.MAX_ATTEMPTS[difficulty]
        self.hint_system = HintSystem(self.secret_word)
        self.start_time = None

    def calculate_score(self, time_taken):
        base = self.BASE_SCORES[self.difficulty]
        penalty = (self.MAX_ATTEMPTS[self.difficulty] - self.attempts_left) * 10
        return max(base - penalty - int(time_taken), 0)

    def play(self):
        self.start_time = time.time()
        print(Fore.GREEN + f"Iniciando jogo para {self.player} no nível {self.difficulty}!")
        logging.info(f"Jogo iniciado: {self.player}, {self.difficulty}, palavra={self.secret_word}")
        while self.attempts_left > 0:
            guess = input(Fore.WHITE + "Digite sua tentativa (ou 'dica'): ").strip().lower()
            if guess == 'dica':
                print(Fore.MAGENTA + self.hint_system.get_hint())
                continue
            if guess == self.secret_word:
                time_taken = time.time() - self.start_time
                score = self.calculate_score(time_taken)
                print(Fore.GREEN + Style.BRIGHT + f"Parabéns {self.player}! Você acertou em {round(time_taken,2)}s. Pontuação: {score}")
                logging.info(f"Vitória: pontos={score}, tempo={round(time_taken,2)}")
                return score, time_taken
            self.attempts_left -= 1
            print(Fore.RED + f"Errado! Tentativas restantes: {self.attempts_left}")
            logging.warning(f"Tentativa errada: {guess}, restantes={self.attempts_left}")
        print(Fore.RED + Style.BRIGHT + f"Fim de jogo! A palavra era '{self.secret_word}'.")
        logging.info("Fim de jogo: sem tentativas")
        return 0, time.time() - self.start_time

def main():
    print(Fore.CYAN + Style.BRIGHT + "=== Jogo de Adivinhação de Palavras ===")
    hs_manager = HighScoreManager()
    while True:
        print(Fore.WHITE + "1. Jogar\n2. Ver recordes\n3. Sair")
        choice = input("Escolha uma opção: ").strip()
        if choice == '1':
            name = input("Digite seu nome: ").strip()
            print("Selecione a dificuldade: 1. Fácil 2. Média 3. Difícil")
            diff_choice = input("Opção: ").strip()
            diff_map = {'1': 'Easy', '2': 'Medium', '3': 'Hard'}
            difficulty = diff_map.get(diff_choice, 'Easy')
            score, time_taken = Game(name, difficulty).play()
            if score > 0:
                hs_manager.add_score(name, score, difficulty, time_taken)
        elif choice == '2':
            hs_manager.display_scores()
        elif choice == '3':
            print(Fore.CYAN + "Obrigado por jogar!")
            break
        else:
            print(Fore.YELLOW + "Escolha inválida. Selecione 1, 2 ou 3.")

if __name__ == "__main__":
    main()

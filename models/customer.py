import random


class Customer:

    def __init__(self):

        self.feedback = ""

        self.customers_data = [

            {
                "name": "Dona Amélia",

                "hint": (
                    "Quero algo redondo, assado e dividido "
                    "em partes... mas hoje só consigo comer metade."
                ),

                "correct_slices": 2,

                "success_feedback": (
                    "Perfeito! Isso me lembra os velhos tempos..."
                ),

                "error_feedback": (
                    "Hmm... acho que veio mais do que eu queria."
                )
            },

            {
                "name": "Garoto Theo",

                "hint": (
                    "Estou sem muita fome hoje... "
                    "quero apenas um pedaço."
                ),

                "correct_slices": 1,

                "success_feedback": (
                    "Boa! Agora consigo comer tudo!"
                ),

                "error_feedback": (
                    "Nossa... isso é comida demais pra mim."
                )
            },

            {
                "name": "Senhor Ramos",

                "hint": (
                    "Hoje trabalhei demais. "
                    "Quero quase a pizza inteira."
                ),

                "correct_slices": 3,

                "success_feedback": (
                    "Excelente. Exatamente como pedi."
                ),

                "error_feedback": (
                    "Você não prestou atenção no pedido."
                )
            }
        ]

        self.generate_customer()

    def generate_customer(self):

        customer = random.choice(self.customers_data)

        self.name = customer["name"]

        self.order = customer["hint"]

        self.correct_slices = customer["correct_slices"]

        self.success_feedback = customer["success_feedback"]

        self.error_feedback = customer["error_feedback"]
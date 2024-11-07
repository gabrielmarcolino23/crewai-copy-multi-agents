#!/usr/bin/env python
import sys
from copywhatsapp.crew import CopywhatsappCrew

def run():
    """
    Run the crew.
    """
    inputs = [
        {
        'objetivo': 'Divulgar a promoção de 50% de desconto em itens selecionados da coleção de verão.',
        'tom_de_voz': 'Cativante',
        'publico_alvo': 'Clientes que compraram na última estação e têm interesse em moda e tendências.'
        },
        {
        'objetivo': 'Anunciar o lançamento da nossa nova linha de produtos sustentáveis.',
        'tom_de_voz': 'Formal',
        'publico_alvo': 'Consumidores preocupados com sustentabilidade e qualidade.'
        }

    ]
    CopywhatsappCrew().crew().kickoff_for_each(inputs=inputs)

def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = [
        {
            'objetivo': 'Agradecer o cliente pela compra e oferecer um giftback',
            'tom_de_voz': 'Amigável',
            'publico_alvo': 'Clientes recorrentes'
        },
        {
            'objetivo': 'Oferecer um giftback para incentivar uma nova compra.',
            'tom_de_voz': 'Cativante',
            'publico_alvo': 'Clientes que compraram recentemente'
        },
        {
            'objetivo': 'Enviar um giftback como parte de um programa de fidelidade.',
            'tom_de_voz': 'Formal',
            'publico_alvo': 'Clientes de alto valor'
        },
        {
            'objetivo': 'Agradecer pela compra e pedir feedback.',
            'tom_de_voz': 'Amigável',
            'publico_alvo': 'Clientes de primeira compra'
        },
        {
            'objetivo': 'Garantir a satisfação do cliente e convidar para seguir no Instagram.',
            'tom_de_voz': 'Informal',
            'publico_alvo': 'Homens de 15 a 22 que gostam de rap'
        },
        {
            'objetivo': 'Confirmar a entrega do produto e oferecer suporte adicional.',
            'tom_de_voz': 'Formal',
            'publico_alvo': 'Clientes corporativos'
        },
        {
            'objetivo': 'Anunciar um novo produto e incentivar a primeira compra',
            'tom_de_voz': 'Cativante',
            'publico_alvo': 'Clientes de moda jovem'
        },
        {
            'objetivo': 'Divulgar um novo produto de edição limitada',
            'tom_de_voz': 'Formal',
            'publico_alvo': 'Clientes de luxo'
        },
        {
            'objetivo': 'Apresentar um novo produto com desconto especial de lançamento.',
            'tom_de_voz': 'Informal',
            'publico_alvo': 'Jovens adultos, 25-35 anos'
        },
        {
            'objetivo': 'Introduzir uma nova coleção com peças exclusivas.',
            'tom_de_voz': 'Cativante',
            'publico_alvo': 'Clientes de alta moda'
        },
        {
            'objetivo': 'Anunciar o lançamento de uma coleção sazonal (ex: primavera/verão)',
            'tom_de_voz': 'Amigável',
            'publico_alvo': 'Mulheres entre 30-45 anos'
        },
        {
            'objetivo': 'Apresentar uma coleção colaborativa com um designer famoso.',
            'tom_de_voz': 'Formal',
            'publico_alvo': 'Clientes de moda premium'
        },
        {
            'objetivo': 'Desejar boas festas e oferecer um desconto especial',
            'tom_de_voz': 'Amigável',
            'publico_alvo': 'Todos os clientes'
        },
        {
            'objetivo': 'Celebrar o Dia dos Namorados com uma promoção especial',
            'tom_de_voz': 'Cativante',
            'publico_alvo': 'Jovens casais'
        },
        {
            'objetivo': 'Oferecer promoções de Dia das Mães com sugestões de presentes.',
            'tom_de_voz': 'Amigável',
            'publico_alvo': 'Filhos adultos, 25-40 anos'
        },
        {
            'objetivo': 'Parabenizar o cliente pelo aniversário com um desconto exclusivo',
            'tom_de_voz': 'Amigável',
            'publico_alvo': 'Clientes de qualquer idade'
        },
        {
            'objetivo': 'Celebrar o aniversário do cliente com um presente surpresa.',
            'tom_de_voz': 'Cativante',
            'publico_alvo': 'Clientes VIP'
        },
        {
            'objetivo': 'Oferecer uma experiência personalizada como presente de aniversário',
            'tom_de_voz': 'Formal',
            'publico_alvo': 'Clientes de alto valor e recorrentes'
        }
    ]

    try:
        CopywhatsappCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        CopywhatsappCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'objetivo': 'Criar um copy para venda de curso de direito',
        'tom_de_voz': 'formal',
        'publico_alvo': 'estudantes de direito'
    }
    try:
        CopywhatsappCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

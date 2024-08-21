from setuptools import setup, find_packages

setup(
    name='mqtt_client_lib',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'paho-mqtt',
        'matplotlib',
    ],
    author='Felipe Canin Novaes',
    author_email='felipe@felipecncloud.com',
    description='Uma biblioteca eficaz que permite desenvolvedores visualizar mensagens do protocolo MQTT em tempo real, facilitando a compreensão da troca de dados.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/felipecaninnovaes/mqtt_graph_lib',  # Atualize com o URL do repositório
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
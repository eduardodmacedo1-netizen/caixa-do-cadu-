# Site G.M. Pádua Advogados

Site estático de página única. Para publicar, envie para a hospedagem o arquivo `index.html` e a pasta `assets/`.

- Não usa banco de dados, formulário, cookies nem serviços externos (fontes e ícones ficam hospedados no próprio site).
- Tema claro e escuro automáticos, conforme a configuração do aparelho do visitante.
- Para abrir no computador, dê dois cliques em `index.html`.

## Como editar

O conteúdo fica em `src/index.template.html` (textos fixos) e `src/build.py` (sócios, temas de conteúdo e lista de áreas).
Depois de editar, rode `python3 site/src/build.py` para gerar o `index.html`.

Ícones: Phosphor Icons, licença MIT (`assets/icons/LICENSE-phosphor.txt`).

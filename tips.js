document.getElementById('btn-tip').addEventListener('click', () => {
    fetch('https://api.adviceslip.com/advice')
        .then(response => response.json())
        .then(data => {
            const dica = data.slip?.advice ?? 'Conteudo nao encontrado';
            document.getElementById('tip-output').innerText = `Sugestao: ${dica}`;
        })
        .catch(() => {
            document.getElementById('tip-output').innerText = 'Erro ao carregar a sugestao.';
        });
});

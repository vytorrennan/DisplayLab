(function () {

    /* tamanho de fonte */
    const STEP = 10, MIN = 80, MAX = 130, KEY = 'dl-font-size';
    const saved = parseInt(localStorage.getItem(KEY)) || 100;
    document.documentElement.style.fontSize = saved + '%';

    function currentSize() { return parseInt(document.documentElement.style.fontSize) || 100; }
    function applySize(size) {
        size = Math.min(MAX, Math.max(MIN, size));
        document.documentElement.style.fontSize = size + '%';
        localStorage.setItem(KEY, size);
    }

    document.getElementById('dl-fonte-maior').addEventListener('click', function (e) { e.preventDefault(); applySize(currentSize() + STEP); });
    document.getElementById('dl-fonte-menor').addEventListener('click', function (e) { e.preventDefault(); applySize(currentSize() - STEP); });
    document.getElementById('dl-fonte-padrao').addEventListener('click',  function (e) { e.preventDefault(); applySize(100); });

    /* toggle do painel */
    const painel = document.getElementById('dl-painel');
    const aba    = document.getElementById('dl-aba');
    const fechar = document.getElementById('dl-fechar');

    aba.addEventListener('click', function () { painel.classList.toggle('open'); });
    if (fechar) fechar.addEventListener('click', function () { painel.classList.remove('open'); });

    /* alto contraste */
    const CONTRASTE_KEY = 'dl-alto-contraste';
    const btnContraste  = document.getElementById('dl-contraste');

    function aplicarContraste(ativo) {
        if (ativo) {
            document.documentElement.classList.add('alto-contraste');
            btnContraste.classList.add('ativo');
            btnContraste.setAttribute('aria-pressed', 'true');
        } else {
            document.documentElement.classList.remove('alto-contraste');
            btnContraste.classList.remove('ativo');
            btnContraste.setAttribute('aria-pressed', 'false');
        }
        localStorage.setItem(CONTRASTE_KEY, ativo ? '1' : '0');
    }

    aplicarContraste(localStorage.getItem(CONTRASTE_KEY) === '1');

    btnContraste.addEventListener('click', function (e) {
        e.preventDefault();
        aplicarContraste(!document.documentElement.classList.contains('alto-contraste'));
    });

})();

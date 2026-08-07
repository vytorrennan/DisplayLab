(function () {

    const STEP = 10, MIN = 80, MAX = 130, FONT_KEY = 'dl-font-size';
    const CONTRASTE_KEY = 'dl-alto-contraste';

    const btnFonteMaior = document.getElementById('dl-fonte-maior');
    const btnFonteMenor = document.getElementById('dl-fonte-menor');
    const btnFontePadrao = document.getElementById('dl-fonte-padrao');
    const btnContraste = document.getElementById('dl-contraste');
    const painel = document.getElementById('dl-painel');
    const aba = document.getElementById('dl-aba');
    const fechar = document.getElementById('dl-fechar');

    function safeLocalStorageGet(key) {
        try {
            return window.localStorage.getItem(key);
        } catch (err) {
            return null;
        }
    }

    function safeLocalStorageSet(key, value) {
        try {
            window.localStorage.setItem(key, value);
        } catch (err) {
            // ignore storage errors
        }
    }

    const saved = parseInt(safeLocalStorageGet(FONT_KEY), 10);
    document.documentElement.style.fontSize = Number.isFinite(saved) ? saved + '%' : '100%';

    function currentSize() { return parseInt(document.documentElement.style.fontSize, 10) || 100; }
    function applySize(size) {
        size = Math.min(MAX, Math.max(MIN, size));
        document.documentElement.style.fontSize = size + '%';
        safeLocalStorageSet(FONT_KEY, size);
    }

    if (btnFonteMaior) {
        btnFonteMaior.addEventListener('click', function (e) { e.preventDefault(); applySize(currentSize() + STEP); });
    }
    if (btnFonteMenor) {
        btnFonteMenor.addEventListener('click', function (e) { e.preventDefault(); applySize(currentSize() - STEP); });
    }
    if (btnFontePadrao) {
        btnFontePadrao.addEventListener('click', function (e) { e.preventDefault(); applySize(100); });
    }

    if (aba && painel) {
        aba.addEventListener('click', function () { painel.classList.toggle('open'); });
    }
    if (fechar && painel) {
        fechar.addEventListener('click', function () { painel.classList.remove('open'); });
    }

    function aplicarContraste(ativo) {
        if (!btnContraste) return;

        if (ativo) {
            document.documentElement.classList.add('alto-contraste');
            btnContraste.classList.add('ativo');
            btnContraste.setAttribute('aria-pressed', 'true');
        } else {
            document.documentElement.classList.remove('alto-contraste');
            btnContraste.classList.remove('ativo');
            btnContraste.setAttribute('aria-pressed', 'false');
        }

        safeLocalStorageSet(CONTRASTE_KEY, ativo ? '1' : '0');
    }

    aplicarContraste(safeLocalStorageGet(CONTRASTE_KEY) === '1');

    if (btnContraste) {
        btnContraste.addEventListener('click', function (e) {
            e.preventDefault();
            aplicarContraste(!document.documentElement.classList.contains('alto-contraste'));
        });
    }

})();

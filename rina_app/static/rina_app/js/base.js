//Recolher e abrir Sidebar
$(document).ready(function () {
    $('#sidebarToggle').on('click', function () {
        $('#sidebar').toggleClass('collapsed');
        $('#content').toggleClass('sidebar-hidden');
    });
});



//adicionar espaçamento para a sidebar
$(document).ready(function () {
    const $navbar = $('.navbar');
    const $sidebar = $('#sidebar');
    const $t_content = $('#template-content');

    function updateMargin() {
        const navbarHeight = $navbar.outerHeight();

        let viewportHeight = window.innerHeight;
        let extraMargin = (viewportHeight * 3) / 100;

        $sidebar.css({
            'margin-top': navbarHeight,
        });
        $t_content.css({
            'margin-top': navbarHeight + extraMargin,
        });
        console.log(navbarHeight)
    }

    let resizeObserver = new ResizeObserver(updateMargin);
    resizeObserver.observe($navbar[0]);
});

//Salvar estado da sidebar
$(document).ready(function () {
    let storedSidebarHTML = sessionStorage.getItem('sidebarHTML');

    $('#sidebar').on('click', 'a.list-group-item', function () {
        saveSidebarHTML();
    });

    function saveSidebarHTML() {
        let sidebarHTML = $('#sidebar').html();

        sidebarHTML = sidebarHTML.replace("highlight", "");

        sessionStorage.setItem('sidebarHTML', sidebarHTML);
    }

    if (storedSidebarHTML) {
        $('#sidebar').html(storedSidebarHTML);
    }
});

//Controle de Highlight na sidebar
$(document).ready(function () {
    $(".list-group-item").hover(
        function () {
            $(this).toggleClass("highlight");
        },
    );
});
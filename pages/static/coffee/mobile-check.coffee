if window.is_mobile
    mobile = $('<div class="go-mobile">
                <p>Looks like you are using a small screen.</p>
                <p>
                    <a href="http://apps.pixtas.com/125760494113916/">mobile-optimized site</a>
                    <a href="#">desktop site</a>
                </p></div>').click -> mobile.remove()

    $('body').prepend mobile

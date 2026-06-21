document.addEventListener(
    'DOMContentLoaded',
    function () {

        const modal =
            document.getElementById(
                'login-modal'
            );

        const openButtons =
        document.querySelectorAll(
            '.js-open-login-modal'
        );

        console.log(openButtons);

        const cancelButton =
            document.querySelector(
                '.modal-cancel'
            );

        openButtons.forEach(
            button => {

                button.addEventListener(
                    'click',
                    function () {

                        modal.classList.add(
                            'active'
                        );

                    }
                );

            }
        );

        cancelButton.addEventListener(
            'click',
            function () {

                modal.classList.remove(
                    'active'
                );

            }
        );

        modal.addEventListener(
            'click',
            function (event) {

                if (
                    event.target === modal
                ) {

                    modal.classList.remove(
                        'active'
                    );

                }

            }
        );

    }
);

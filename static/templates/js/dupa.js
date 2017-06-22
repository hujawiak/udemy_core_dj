    $(document).ready(function () {
        $(".site-wrapper").fadeIn({
            "duration": 400,
            "easing": "easeInBounce"
        });
        $clicked = 0;
        $(".defaultLink").click(function (event) {
            event.preventDefault();
            //alert("prevented default");
            $clicked ++;
            $nosacze = ["http://zasoby.ekologia.pl/artykulyNew/15191/xxl/nosacz-wikicc_800x600.jpg",
            "http://dinoanimals.pl/wp-content/uploads/2013/09/Nosacz9.jpg"];
            $l = "";
            $(".active a").css("color", "red");

            if($clicked % 2 === 0) {
                $l = $nosacze[0];

                $(".masthead-brand").fadeIn();
            }
            else {
                $l = $nosacze[1];
            }
            $("#nosacz").attr("src", $l).attr("width", "500px");

        });
        $("#features").click(function (event) {
            event.preventDefault();
            $("p.lead").fadeToggle("slow", function () {
                    $(this).text("DUPA");
                }
            ).fadeToggle("slow");
        })
    });

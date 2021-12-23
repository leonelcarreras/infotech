var owl = $('#staff');
              owl.owlCarousel({
                margin:20,
                dots:true,
                nav: true,
                navText: [
                  "<i class='fa fa-chevron-left'></i>",
                  "<i class='fa fa-chevron-right'></i>"
                ],
                autoplay: true,
                autoplayHoverPause: true,
                responsive: {
                  0: {
                    items: 1
                  },
                  600: {
                    items: 2
                  },
                  1000: {
                    items:2
                  },
                  1200: {
                    items:4
                  }
                }
  });
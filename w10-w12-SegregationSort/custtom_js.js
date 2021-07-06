/**************************************************************************
 * helper functions (vanilla js)
 **************************************************************************/
function windowIsMobile(mobileWidth = "1024") {
    if (window.matchMedia(`screen and (max-width: ${mobileWidth})`).matches) {
        return false
    } else {
        return true
    }
}

function siteHeaderIsVisible() {
    // figure this out
    return true
}

/**************************************************************************
 * begin jQuery
 **************************************************************************/
document.addEventListener('DOMContentLoaded', function() {
    jQuery(function($) {

        /******************************************************************
         * define
         ******************************************************************/
        // The collection of all the sections in the page's accordion
        let accordionItems = document.querySelectorAll(
            '.bdt-accordion-item');
        // The title elements of each item in accordionItems
        let accordionTitles = document.querySelectorAll(
            '.bdt-accordion-item .bdt-accordion-title');

        // initialize the following items, set them in setAllItems()
        let accordionOpenIndex = -1;
        let bdtOpen, bdtOpenTitle;
        let secondTitle, marginTop;
        let headerHeight, accordionTitleHeight;
        let distanceToFirstAccordion;

        // all update functionality here
        function updateSpacingVariables() {
            // update accordionOpenIndex
            accordionOpenIndex = parseInt(
                bdtOpenTitle.getAttribute('data-accordion-index')
            )

            // get ".bdt-open" child element again
            bdtOpen = document.querySelector('.bdt-open');
            bdtOpenTitle = bdtOpen.firstElementChild;

            // get margin spacing between accordion elements (if multiple)
            secondTitle = document.querySelector(
                '.bdt-accordion > :nth-child(2)');
            marginTop = parseInt(getComputedStyle(secondTitle).marginTop);

            // take the site header spacing into account
            headerHeight = parseInt(
                document.querySelector('.elementor-1396').offsetHeight);
            if (windowIsMobile())
                headerHeight = 0 // header is hidden on mobile

            // get height for a single accordion element 
            accordionTitleHeight = bdtOpenTitle.offsetHeight;

            // variable to keep track of how much to scroll to first 
            // accordion tab in px
            distanceToFirstAccordion = $(
                '.bdt-accordion > :nth-child(1)'
            ).offset().top - headerHeight;

            // debug
            console.log(
                "Offset of first accordion item is " +
                $('.bdt-accordion > :nth-child(1)').offset().top,

                "distanceToFirstAccordion is " +
                distanceToFirstAccordion,

                "accordionTitleHeight is " + accordionTitleHeight,

                "headerHeight is " + headerHeight
            )
        }

        // set all the items for the first time as defined above
        updateSpacingVariables()

        /******************************************************************
         * Loop through accordion items and 
         * add the class "is-empty" to the blank ones
         ******************************************************************/
        accordionItems.forEach((items, index) => {
            var titleSpans = accordionTitles[index].querySelectorAll(
                '.bdt-flex');
            var titleSpansMod = titleSpans[0].textContent.replace(
                /\s/g, '');

            // we will let css hide each empty accordion section 
            // we just need to flag which sections are empty
            if (titleSpansMod == "") items.classList.add('is-empty');
        })

        /******************************************************************
         * animate
         ******************************************************************/
        let fps = 60

        accordionItems.forEach((items, index) => {

                // to be called when accordion item is clicked
                items.onclick = function() {

                        // thread to make sure timing is consistent
                        setTimeout(function() {

                            // update the spacing variables to match page
                            updateSpacingVariables()

                            // get snapshot of current window scrollY
                            let scrollYCurrent = window.scrollY

                            // is there an open accordion?
                            let accordionIsOpen = accordionOpenIndex >= 0;
                            if (accordionIsOpen) {

                                // amount to scroll so that desired element
                                // is visible at top of page (under header)
                                let scrollAmount = (
                                    distanceToFirstAccordion +
                                    accordionOpenIndex *
                                    (accordionTitleHeight + marginTop)
                                )

                                // do we scroll up or down?
                                let scrollDirection = Math.sign(
                                    scrollYCurrent - scrollAmount)

                                // ** scrollYCurrent is the current 
                                // y position of window top on page
                                // ** scrollAmount is the desired 
                                // y position for window top on page

                                // animate scroll down
                                if (scrollDirection < 0) {
                                    // set timed loop for incrementation
                                    let loop = setInterval(() => {
                                        // console.log("scrolling down...")

                                        // incrementally scroll down 10px
                                        window.scroll(0, scrollYCurrent)
                                        scrollYCurrent += 10

                                        // if current pos is below/at target
                                        // (was previously above)
                                        if (scrollYCurrent >= scrollAmount)
                                            clearInterval(loop) // exit loop

                                    }, 1000 / fps); // end setInterval()

                                    return
                                }

                                // animate scroll up
                                if (scrollDirection > 0) {
                                    // set timed loop for incrementation
                                    let loop = setInterval(function() {
                                        // console.log("scrolling up...")

                                        // incrementally scroll down 10px
                                        window.scroll(0, scrollYCurrent)
                                        scrollYCurrent -= 10

                                        // if current pos is above/at target
                                        // (was previously below)
                                        if (scrollYCurrent >= scrollAmount)
                                            clearInterval(loop) // exit loop

                                    }, 1000 / fps); // end setInterval()

                                    // now we're in the desired location, 
                                    // compensate a bit more
                                    setTimeout(() => {
                                            if (!siteHeaderIsVisible()) return
                                            let scrollAnimationDuration = .4 // sec
                                            let scrollAnimationDelay = 2 // sec
                                            $(window).scrollTop(
                                                $(window).animate({
                                                        scrollTop: scrollAmount
                                                    },
                                                    1000 * scrollAnimationDuration
                                                )
                                            )
                                        }, .8 * 1000) // scroll animation delay (in seconds*1000ms)
                                }

                            } // end if
                        }, 1000 / fps); // end setTimeout()
                    } // end lambda (onclick override)
            }) // end foreach loop

        /******************************************************************
         * Automate creation of url parameters for verse groups
         * Find span with the title within accordian titles div
         ******************************************************************/
        let accordionTitleSpans = $(
            '.bdt-accordion-item .bdt-accordion-title .bdt-flex');

        // Set arrays to the same length as accordionTitleSpans, 
        // to be overwritten later
        var titleSpansHyphen = Array.from(accordionTitleSpans);
        var titleSpansComplete = Array.from(accordionTitleSpans);
        var strings = Array.from(accordionTitleSpans);

        // Automate creation of URL parameters
        for (i = 0, j = 0; i < accordionTitles.length; i++, j++) {
            // Remove empty verse titles and groups from strings array
            if (accordionTitleSpans[j].textContent.replace(/\s/g, '') == "") {
                strings.splice(j, 1);
                j--;
                continue;
            }

            // Replace space after "Verse" with hyphen
            if (accordionTitleSpans[i].textContent.search("Verse ") !== -1) {
                titleSpansHyphen[i] = (
                    accordionTitleSpans[i].textContent.replace(
                        "Verse ", "Verse-"))
            }

            // Replace space after "Verses" with hyphen
            if (accordionTitleSpans[i].textContent.search("Verses ") !== -1) {
                titleSpansHyphen[i] = (
                    accordionTitleSpans[i].textContent.replace(
                        "Verses ", "Verses-"))
            } else {
                titleSpansHyphen[i] = accordionTitleSpans[i].textContent;
            }

            // Remove excess spaces  
            titleSpansComplete[i] = String(
                titleSpansHyphen[i]).replace(/\s/g, '');
            console.log(titleSpansHyphen[i])

            // Add question mark at beginning and store 
            // URL parameters within strings variable  
            strings[i] = "?".concat(titleSpansComplete[i]);
        }

        /*******************************************************************
         * open accordion tab which corresponds to 
         * verse group specified in url
         * (Alejandro's code)
         *******************************************************************/
        strings.forEach((title, index) => {
            if (window.location.href.indexOf(title) >= 0) {
                $(accordionTitles).eq(index).click()

                accordionOpenIndex = i
            }
        })

    });
}); // end jQuery
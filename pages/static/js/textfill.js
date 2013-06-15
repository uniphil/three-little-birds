(function($) {
    $.fn.textfill = function(maxFontSize) {
        console.log('filling....');
        maxFontSize = parseInt(maxFontSize, 100);
        return this.each(function(){
            var ourText = $("span", this),
                parent = ourText.parent(),
                maxWidth = parent.width(),
                fontSize = parseInt(ourText.css("fontSize"), 6),
                multiplier = maxWidth/ourText.width(),
                newSize = (fontSize*(multiplier-0.1));
            ourText.css(
                "fontSize",
                (maxFontSize > 0 && newSize > maxFontSize) ? maxFontSize : newSize
            );
        });
    };
})(jQuery);

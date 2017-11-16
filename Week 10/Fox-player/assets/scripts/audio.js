'use strict'

const audio = function() {
    const audio = document.querySelector( "audio" );
    let selectedSong = 0;

    const audioPlay = function ( data, i ) {
        audio.autoplay = "autoplay";
        selectedSong = i;
        console.log(selectedSong)
        if (selectedSong > data.length - 1 ) {
            selectedSong = 0;
            audio.src = data[0].path;
        } else if (selectedSong < 0) {
            selectedSong = data.length - 1;
            audio.src = data[selectedSong].path;
        } else {
            audio.src = data[i].path;
        };

        console.log( data.length, selectedSong )
    };

    const listSelecting = function( data ) {
    
        const selectCurrent = function( element, i, itemList, className ) {
            element.addEventListener( 'dblclick', function() {
                console.log(element)
                console.log(i)
                console.log(itemList)
                console.log(className)
                const selected = document.querySelector( `.${className}` );
                if ( selected ) {selected.classList.remove( `${className}` )};
                this.classList.add( className );
                if ( className == "selected_song" ) {
                    audioPlay( data, i )
                };
            });
        }
        
        const selectBoss = function( itemList, className ) {
            itemList.forEach( function( element, i ) {
                selectCurrent( element, i, itemList, className )
            });
            // onAudioEnd( data, i );
        };
    
        let listsAll = document.querySelectorAll( ".list" );
        let songsAll = document.querySelectorAll( ".song" );
        
        const addClickFunc = function() {
            selectBoss( listsAll, "selected_list" );
            selectBoss( songsAll, "selected_song" );
        };
        
        addClickFunc();
    };

    const onAudioEnd = function( data, i ) {
        audio.onended = function(event) {
            audio.src = data[i + 1].path;
        };
    };

    const forward = function( data ) {
        const forwardBtn = document.querySelector( ".forward" );
        forwardBtn.addEventListener('click', function() {
            audioPlay( data, selectedSong + 1 )
        });
    };

    const rewind = function( data ) {
        const rewindBtn = document.querySelector( ".rewind" );
        rewindBtn.addEventListener('click', function() {
            audioPlay( data, selectedSong - 1 )
        });
    }

    const audioMaster = function( data ) {
        listSelecting( data );
        forward( data );
        rewind( data );
    };

    return {
        audioMaster
    };
};
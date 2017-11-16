'use strict'

const audio = function() {
    const audio = document.querySelector( "audio" );
    let selectedSong = 0;

    const playlistsAndSongs = function () {
        let listsAll = document.querySelectorAll( ".list" );
        let songsAll = document.querySelectorAll( ".song" );

        return {
            listsAll,
            songsAll
        };
    };

    const audioPlay = function ( data, i ) {
        audio.src = data[i].path;
        audio.autoplay = "autoplay";
        selectedSong = i;
    };

    const selectCurrent = function( element, i, className, data ) {
        const selected = document.querySelector( `.${className}` );
        if ( selected ) {selected.classList.remove( `${className}` )};
        element.classList.add( className );
        if ( className == "selected_song" ) {
            audioPlay( data, i )
        };
    };
    
    const selectBoss = function( itemList, className, data ) {
        itemList.forEach( function( element, i ) {
            element.addEventListener( 'dblclick', function() {
                selectCurrent( element, i, className, data )
            })
        });
    };
    
    const addClickFunc = function( listsAll, songsAll, data ) {
        selectBoss( listsAll, "selected_list", data );
        selectBoss( songsAll, "selected_song", data );
    };

    const forwardFunc = function( data, songsAll ) {
        if ( selectedSong >= songsAll.length - 1 ) {
            selectedSong = 0;
        } else {
            selectedSong = selectedSong + 1
        };
        selectCurrent( songsAll[selectedSong], selectedSong, "selected_song", data )
    }

    const forward = function( data, songsAll ) {
        const forwardBtn = document.querySelector( ".forward" );
        forwardBtn.addEventListener('click', function() {
            forwardFunc( data, songsAll );
        });
        const audio = document.querySelector("audio");
        audio.addEventListener("ended", function() {
            forwardFunc( data, songsAll );
        });
    };

    const rewind = function( data, songsAll ) {
        const rewindBtn = document.querySelector( ".rewind" );
        rewindBtn.addEventListener('click', function() {
            if ( selectedSong <= 0 ) {
                selectedSong = songsAll.length - 1;
            } else {
                selectedSong = selectedSong - 1
            };
            selectCurrent( songsAll[selectedSong], selectedSong, "selected_song", data );
        });
    };

    const ranomiseFunc = function( shuffledData ) {

    };

    const shuffleFunc = function( shuffledData ) {
        const shuffleBtn = document.querySelector( ".shuffle" );
        shuffleBtn.addEventListener( 'click', function() {
            let lists = playlistsAndSongs();
            if ( shuffleBtn.src === "http://localhost:3000/images/shuffle.svg" ) {
                shuffleBtn.src = "images/shuffle2.svg"
                shuffleBtn.classList.add( "shuffle_selected" )
            } else {
                shuffleBtn.src = "images/shuffle.svg";
                if ( shuffleBtn.classList.contains( "shuffle_selected" )) {
                    shuffleBtn.classList.remove( "shuffle_selected" );
                };
            };
            ranomiseFunc( shuffledData );
        });
    };

    const shuffle = function( data ) {
        data.forEach( function( element, i ) {
            let j = Math.floor(Math.random() * ( i + 1 ));
            let temp = element;
            element = data[j];
            data[j] = temp;
        });
        shuffleFunc( data );
    };

    const audioMaster = function( data ) {
        let lists = playlistsAndSongs();
        addClickFunc( lists.listsAll, lists.songsAll, data );
        forward( data, lists.songsAll );
        rewind( data, lists.songsAll );
        shuffle( data );

    };

    return {
        audioMaster
    };
};
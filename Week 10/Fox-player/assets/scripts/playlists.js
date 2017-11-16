'use strict'

const playlistsAndTracks = function( getTimeFormat ) {
    const addListElement = function( element, cls ) {
        const li = document.createElement( "li" );
        li.classList.add( cls );
        li.textContent = element.name
        return li
    }
    
    const renderPlaylist = function( data ) {
        const playlists = document.querySelector( ".playlists" );
        playlists.innerHTML = "";
        data.forEach( function( element ) {
            const li = addListElement( element, "list" );
            if ( element.system === 0 ) {
                li.innerHTML += `<i class="fa fa-times icon" aria-hidden="true"></i>`
            }
            playlists.appendChild( li );
        });
        removePlaylistEvents();
    };
    
    const renderTracks = function( data ) {
        const tracklist = document.querySelector( ".tracklist" );
        data.forEach(  function( element, i ) {
            const index = i + 1;
            const li = addListElement( element, "song" );
            li.innerHTML = `<span class="index">${index}</span>${element.title}`;
            const time = getTimeFormat( element.duration );
            li.innerHTML += `<span class="song_length">${time}</span>`;
            tracklist.appendChild( li );
        });
        audioFunctions.audioMaster( data );
    };

    const playlistAdder = function() {
        const addBtn = document.querySelector( ".fa-plus" );
        const addNew = document.querySelector( ".add_new_playlist" );
        
        addBtn.addEventListener( 'click', function() {
            addNew.classList.toggle( "hidden" )
            if ( !newListInput.classList.contains( "hidden" ) ) {
                newListInput.value = "";
                newListInput.focus();
            };
        });
        
        const newListBtn = addNew.querySelector( "button" );
        const newListInput = addNew.querySelector( "input" );
        
        newListBtn.addEventListener( 'click', function() {
            if ( newListInput.value.length > 0 ) {
                const requestBody = {value: newListInput.value};
                ajax.send( "POST", "/playlists", () => ajax.getPlaylists( renderPlaylist ), requestBody );
                addNew.classList.add( "hidden" );
            }
        });
    };
    
    const removePlaylistEvents = function() {
        const removeButtons = document.querySelectorAll( ".fa-times" );
        removeButtons.forEach( function( element ) {
            element.addEventListener( 'click', function() { 
                const requestBody = {value: element.parentNode.textContent};
                ajax.send( "DELETE", "/playlists", () => ajax.getPlaylists( renderPlaylist ), requestBody );
            }) 
        })
    };
    
    playlistAdder();
    

    ajax.getPlaylists( renderPlaylist );
    ajax.getTracks( renderTracks );

    return {
        renderPlaylist,
        renderTracks
    }
}
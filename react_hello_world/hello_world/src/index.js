import React from 'react';
import ReactDOM from 'react-dom';
// import './style.scss';

class Hello extends React.Component {
    render() {
        return ( 
            <h1>Hello World</h1>
        );
    }
};

ReactDOM.render(
    <Hello />,
    document.querySelector('body')
);
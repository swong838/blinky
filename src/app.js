import React from 'react';
import ReactDOM from 'react-dom';
import Picker from './components/picker';
import TriggerEffect from './components/trigger_effect';
import TestButton from './components/test_button';
import ClearButton from './components/clear_button';

class Brazier extends React.Component {
    render() {
        return (
            <article class="pure-g">
                <div className="pure-u-1-2">
                    <div className="pure-button-group">
                        <ClearButton />
                        <TestButton />
                    </div>
                </div>
                <div className="pure-u-1-2">
                    <div className="pure-button-group">
                        <TriggerEffect label="Candle" effect="candle" />
                        <TriggerEffect label="Orange Lamp" effect="lamp_orange" />
                        <TriggerEffect label="Flare" effect="flare" />
                        <TriggerEffect label="Pulse" effect="pulsered" />
                    </div>
                </div>
                <section className="pure-u-1">
                    <Picker initialColor="rgb(0,0,0,1)" />
                </section>
            </article>
        )
    }
}

ReactDOM.render(<Brazier />, document.getElementById('app'));

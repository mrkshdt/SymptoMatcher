import axios from 'axios';
import React, { useState } from 'react';
import { Button, Spinner, Input } from 'reactstrap';
import route_gif from '../assets/route.gif';

function NavigationPlotter(props) {
    const [navState, setNavState] = useState({
        imageGenerated: false,
        loading: false,
        error: false,
    });
    const [navData, setNavData] = useState({
        userString: "",
        destination: ""
    });

    function handleSubmit() {
        setNavState({
            ...navState,
            loading: true,
        })
        reqImageGen(navData['userString']);
    };

    function reqImageGen(uStr) {
        axios.get(`/api/routing?user_string=${uStr}`)
            .then((res) => {
                setNavState({
                    ...navState,
                    imageGenerated: true,
                    loading: false,
                    error: false,
                });
                let ranking = res.data.ranking
                setNavData({
                    destination: ranking.length > 0 ? ranking[0][0] : ''
                });
            })
            .catch((err) => {
                console.log(err);
                setNavState({
                    ...navState,
                    loading: false,
                    error: true,
                })
            });
    }


    return (

        <div className="text-left">

            <div className="px-1">
                {navState['error'] && <span className="text-danger">Leider ist beim aktualisieren der Navigation ein Fehler aufgetreten</span>}
                {!navState['error'] && !navState['loading'] && <h3>Sie werden zu folgendem Ziel navigiert: <strong>{`${navData['destination']}`}</strong></h3>}
                {!navState['imageGenerated'] &&
                    <form onSubmit={(event) => { event.preventDefault(); handleSubmit(); }}>
                        <Input type="text"
                            name="userString"
                            placeholder="Beschreiben sie ihre Symptome hier..."
                            value={navData['userString']}
                            onChange={(e) => setNavData({
                                ...navData,
                                userString: e.target.value
                            })}
                            rows="3"
                        />

                        <Button color="primary" onClick={handleSubmit} className="mt-2 w-50 h-50 submit-button">
                            {navState['loading'] ? <Spinner color="primary" /> :
                                (navState['imageGenerated'] || navState['error']) ? "Route neu berechnen" :
                                    "Route berechnen"}
                        </Button>
                    </form>}
            </div>
                {navState['imageGenerated'] && <img src={route_gif} alt="invisible..." width="100%"/>}
        </div>

    )
}

export default NavigationPlotter;
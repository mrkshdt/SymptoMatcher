import axios from 'axios';
import React, { useState } from 'react';
import { Button, Spinner, Input } from 'reactstrap';
import route_gif from '../assets/route.gif';
import FunFact from './FunFact'

function NavigationPlotter(props) {
    const [navState, setNavState] = useState({
        imageGenerated: false,
        loading: false,
        error: false,
        showFunFact: false,
    });
    const [navData, setNavData] = useState({
        userString: "",
        destination: "",
        funFact: "",
    });

    function handleSubmit() {
        setNavState({
            ...navState,
            loading: true,
        })
        reqImageGen(navData['userString']);
    };

    function resetFunFact(){
        // imageGenerated is supposed to stay true up to this point so it should not have to be set again, so this is a workaround due to a bug
        setNavState({ ...navState, showFunFact: false, imageGenerated: true});
    }

    function reqImageGen(uStr) {
        axios.get(`/api/routing?user_string=${uStr}`)
            .then((res) => {
                let funFact = res.data.funFact
                setNavState({
                    ...navState,
                    imageGenerated: true,
                    loading: false,
                    error: false,
                    showFunFact: funFact != null ? true : false,
                });
                let ranking = res.data.ranking
                setNavData({
                    ...navData,
                    destination: ranking.length > 0 ? ranking[0][0] : '',
                    funFact: funFact != null ? funFact : '',
                });
                // Set a timeout to turn off the funFact after 3 seconds
                setTimeout(() => resetFunFact(), 3000);
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
                {navState['showFunFact'] && <FunFact text={navData['funFact']} />}

                {!navState['showFunFact'] && <div>
                    {navState['error'] && <span className="text-danger">Leider ist beim aktualisieren der Navigation ein Fehler aufgetreten</span>}
                    {navState['imageGenerated'] ? 
                        <h3>Sie werden zu folgendem Ziel navigiert: <strong>{`${navData['destination']}`}</strong></h3> :
                        <h3>Bitte geben sie ihr Anliegen oder ihre Symptome ein</h3> 
                    }
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
                    {navState['imageGenerated'] && <img src={route_gif} alt="invisible..." width="100%" />}
                </div>}


            </div>

        </div>

    )
}

export default NavigationPlotter;
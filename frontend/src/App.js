import React from 'react';
import logo from './logo.svg';
import './App.css';

import {Link} from "react-router-dom"

import USAMap from "react-usa-map";

import ELECTORAL_VOTES from "./electoral_votes"

import {Button, TextField} from "@material-ui/core"

function getCookie(name) {

    const test_name = document.cookie

    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';')

        for(let i = 0;i < cookies.length; i++) {
            let cookie = cookies[i]
            let [cookieName, val] = cookie.split("=")
            cookieName = cookieName.trim()
            if(name===cookieName) return val
        }
    }

    return null

}

const getParamsFromURL = (paramsStr) => {
    let parameters = {}

    if(paramsStr) paramsStr.split("?")[1].split("&").forEach(part => {
        let item = part.split("=")
        parameters[item[0]] = decodeURIComponent(item[1])
    })

    return parameters

}



function App(props) {

    const [loadingStatus, setLoadingStatus] = React.useState(0)
    const [states, setStates] = React.useState({})
    const [electoralVotes, setElectoralVotes] = React.useState({
        democrats: 0,
        republicans: 0,
    })
    const [saveMessage, setSaveMessage] = React.useState("")
    const [baseUrl, setBaseUrl] = React.useState("")
    const [shareUrl, setShareUrl] = React.useState("")
    const [copied, setCopied] = React.useState(false)
    const [username, setUsername] = React.useState(undefined)

  const isFilled = Object.keys(states).length == 51

  const today = new Date()
  const canSave = today < new Date(2020, 10, 3)

  const viewId = getParamsFromURL(props.location.search)['view_id']

  React.useEffect(() => {
    const fetchUserPrediction = async () => {
        let res
        if(!viewId) res = await fetch(`/load/`)
        else res = await fetch(`/load/?view_id=${viewId}`)
        if(res.status === 403) setLoadingStatus(2)
        else {
            const raw_data = await res.json()
            const base_url = raw_data.base_url
            setBaseUrl(base_url)
            let json_data = JSON.parse(raw_data.prediction)
            setShareUrl(`${base_url}/static/build/index.html?view_id=${json_data.id}`)

            setUsername(raw_data.username)
            delete json_data.number_correct
            delete json_data.id
            delete json_data.user
            json_data.ID = json_data.IDA
            delete json_data.IDA
            setElectoralVotes({democrats: json_data.electoral_votes_dem, republicans: json_data.electoral_votes_rep})
            delete json_data.electoral_votes_dem
            delete json_data.electoral_votes_rep
            setStates(json_data)
            setLoadingStatus(1)
        }
    }

    fetchUserPrediction()
  }, [])

  const mapHandler = (event) => {
    if(!viewId){
        setSaveMessage("")
        const stateId = event.target.dataset.name == 'DC' ? 'DC2' : event.target.dataset.name
        let newStates = JSON.parse(JSON.stringify(states))
        if (stateId in newStates) {
            if(newStates[stateId].fill === 'navy') {
                newStates[stateId].fill = 'red'
                setElectoralVotes({
                    democrats: electoralVotes.democrats - ELECTORAL_VOTES[stateId],
                    republicans: electoralVotes.republicans + ELECTORAL_VOTES[stateId],
                })
            }
            else {
                newStates[stateId].fill = 'navy'
                setElectoralVotes({
                    democrats: electoralVotes.democrats + ELECTORAL_VOTES[stateId],
                    republicans: electoralVotes.republicans - ELECTORAL_VOTES[stateId],
                })
            }
        } else {
            newStates[stateId] = {'fill': 'navy'}
            setElectoralVotes({...electoralVotes, democrats: electoralVotes.democrats + ELECTORAL_VOTES[stateId]})
        }
        setStates(newStates)
    }
  };
  return (
    <div className="App">
        {loadingStatus === 0 ? "Loading" : loadingStatus === 2 ? "Not Logged in properly, or invalid ID, unable to load" : loadingStatus === 1 && (
            <>
                <div style={{position: "relative", marginTop: '50px'}}>
                    <div style={{position: "absolute", left: "0px" , top:"10px", height: '40px', width: `${electoralVotes.republicans / 538 * 100}%` , background: "red"}}></div>
                    <div style={{position: "absolute", right: "0px" , top:"10px", height: '40px', width: `${electoralVotes.democrats / 538 * 100}%` , background: "navy"}}></div>
                    <div style={{position: "absolute", left:"5%", top:"0px", color: '#999' }}>
                        <h3>Republicans: {electoralVotes.republicans}</h3>
                    </div>

                    <div style={{position: "absolute", right:"5%", top:"0px", color: '#999'}}>
                        <h3>Democrats: {electoralVotes.democrats}</h3>
                    </div>
                    {viewId !== undefined && (
                    <div style={{paddingTop: '100px'}}>
                        <h1>{username}'s map</h1>
                    </div>
                    )}
                    <div style={{paddingTop: '100px'}}>
                        <USAMap customize={states} onClick={mapHandler}  />
                    </div>
                </div>
                {canSave ? (
                    <>
                        <div>
                            {viewId === undefined && <Button
                                onClick={async ev => {
                                    const csrf_token = getCookie("csrftoken")

                                    const res = await fetch(`/save/`, {
                                        method: 'POST',
                                        mode: 'cors',
                                        headers: {
                                            'X-CSRFToken': csrf_token,
                                            'Content-Type': 'application/json',
                                        },
                                        body: JSON.stringify({states: states, electoralVotes: electoralVotes})
                                    })
                                    if(res.status === 200) setSaveMessage("Saved! You're all set! (You can modify it until November 3rd)")
                                    else setSaveMessage("Did not save properly!  Please try clicking save again")
                                }}
                                variant="contained" disabled={!isFilled} color="primary" style={{marginTop: '50px'}}>
                                {isFilled ? "Save My Prediction" : "Not Finished"}
                            </Button>}
                        </div>
                        {viewId === undefined && <div style={{marginTop: '50px'}}>
                           <p>Share Link</p>
                           <TextField
                            value={shareUrl}
                            style={{width: '75%'}}
                            onClick={ev => {
                                ev.target.select()
                                document.execCommand('copy')
                                setCopied(true)
                                setTimeout(()=> {
                                    setCopied(false)
                                }, 1500)
                            }}
                           />
                        </div>}
                        {viewId === undefined && <p style={{paddingBottom: '200px'}}>{copied ? "Copied!" : "Click to copy to Clipboard"}</p>}
                        {viewId !== undefined && canSave && <div style={{marginTop: '50px'}}>
                            This is {username}'s prediction for the 2020 election, what's yours?  Give it a try yourself here!
                            <div style={{paddingBottom: '200px'}}>
                                <Link to={`//${baseUrl}`} target="_blank">
                                    Predict the Election
                                </Link>
                            </div>
                        </div>}
                    </>
                ) : (
                    viewId === undefined && <p>It is November 3rd (Or after) and you can't update your prediction anymore.</p>
                )}

                <p>{saveMessage}</p>
            </>
        )}


    </div>
  );
}

export default App;

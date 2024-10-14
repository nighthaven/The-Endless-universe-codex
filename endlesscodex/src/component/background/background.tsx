import {useEffect, useState} from "react";

import "./background.scss";

interface Firefly {
    id: number;
    top: string;
    left: string;
    animationDuration: string;
}

const createFirefly = (): Firefly => ({
        id: Math.random(),
        top: `${Math.random() * 100}%`,
        left: `${Math.random() * 100}%`,
        animationDuration: `${Math.random()*5 + 5}s`,
})

const BackgroundComponent = () => {
    const [fireflies, setFireflies] = useState<Firefly[]>([]);
    useEffect(() => {
        const addFireflyPeriodically = () => {
            const newFirefly = createFirefly();
            setFireflies(currentFireflies => [...currentFireflies.slice(-14), newFirefly]);
        }

        const interval = setInterval(addFireflyPeriodically, 1000);
        return () => clearInterval(interval);
    }, [])

    return (
        <div className="background">
            {fireflies.map((firefly) => {
                return (
                    <div
                        key={firefly.id}
                        className="firefly-background"
                        style={{top: firefly.top, left: firefly.left, animation: `move ${firefly.animationDuration} infinite alternate`}}
                    ></div>
                );
            })}
        </div>
    )}

export default BackgroundComponent;
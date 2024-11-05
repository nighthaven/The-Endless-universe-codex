import React, { Fragment, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { selectFireflies } from "../../store/background/background.selector";
import { addFirefly } from "../../store/background/background.reducer";

import "./firefly.styles.scss";

const createFirefly = () => ({
    id: Math.random(),
    top: `${Math.random() * 100}%`,
    left: `${Math.random() * 100}%`,
    animationDuration: `${Math.random() * 5 + 5}s`,
});

const FireflyComponent = () => {
    const dispatch = useDispatch();
    const fireflies = useSelector(selectFireflies);

    useEffect(() => {
        const addFireflyPeriodically = () => {
            const newFirefly = createFirefly();
            dispatch(addFirefly(newFirefly));
        };

        const interval = setInterval(addFireflyPeriodically, 1000);
        return () => clearInterval(interval);
    }, [dispatch]);

    return (
        <Fragment>
            {fireflies.map((firefly) => {
                return (
                    <div
                        key={firefly.id}
                        className="firefly-background"
                        style={{
                            top: firefly.top,
                            left: firefly.left,
                            animation: `move ${firefly.animationDuration} infinite alternate`,
                        }}
                        data-testid="firefly-component"
                    ></div>
                );
            })}
        </Fragment>
    );
};

export default FireflyComponent;

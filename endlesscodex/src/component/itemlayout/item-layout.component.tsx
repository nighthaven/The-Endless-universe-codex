"use client";
import { motion } from "framer-motion";
import clsx from "clsx";
import { ReactNode, FC, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { RootState } from "../../store/store";
import { showItem, hideItem } from "../../store/item-layout/item-layout.reducer"; // Import des actions

interface ItemLayoutProps {
  children: ReactNode;
  className?: string;
}

const ItemLayoutComponent: FC<ItemLayoutProps> = ({ children, className }) => {
  const dispatch = useDispatch();
  const isVisible = useSelector((state: RootState) => state.item.visible); // Sélection de l'état

  useEffect(() => {
    // Simule un changement de visibilité quand l'item est monté
    dispatch(showItem());

    return () => {
      dispatch(hideItem());
    };
  }, [dispatch]);

  return (
    <motion.div
      initial={{ scale: 0 }}
      animate={{ scale: isVisible ? 1 : 0 }}  // Animation basée sur l'état Redux
      transition={{ duration: 0.5 }}
      className={clsx(
        "custom-bg p-6 sm:p-8 rounded-xl flex items-center justify-center space-y-8",
        className
      )}
    >
      {children}
    </motion.div>
  );
};

export default ItemLayoutComponent;
